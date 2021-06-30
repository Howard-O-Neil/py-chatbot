from datetime import datetime, timedelta
from uuid import uuid4
from entities.task import Task

from flask import app
from entities.iteration import Iteration
from application.share.dialog_utils import DialogUtils, dialogUtils
from werkzeug.exceptions import NotFound
from application.share.utils import stdout, utils
from entities.user import User
from .repository import repository
from entities.project import Project
from app import fake
import click
import json


class Service:
    @utils.handle_service_error
    def sign_up_project_token(self, data):
        stdout(data)

        return {
            "message": "failed"
        }

    @utils.handle_service_error
    def add_project(self, data):
        project = Project(
            name=data["name"],
            estimated_hours=1000.0,
            slack_team_id=data["slack_team_id"],
            description=fake.paragraph(nb_sentences=5),
            goal=fake.text(max_nb_chars=100),
        )

        inserted_proj = repository.add_data_flush(project)

        for i in range(int(1000 / 200)):
            iteration_status = ""
            if i == 0: iteration_status = "Processing"
            else: iteration_status = "NotStarted"

            iteration = Iteration(
                id=uuid4(),
                project_id = inserted_proj.id,
                start_date = datetime.now() + timedelta(hours=200 * i),
                status = iteration_status,
                name = fake.company(),
                goal = fake.text(max_nb_chars=100),
                description = fake.paragraph(nb_sentences=5),
                velocity = 1.0,
                point = 300.0,
                estimated_hours = 400.0,
                logged_hours = 0.0
            )
            inserted_iteration = repository.add_data_flush(iteration)

            for i in range(200):
                task = Task(
                    id=uuid4(),
                    backlog_id = None,
                    assignee = None,
                    iteration_id = inserted_iteration.id,
                    type = "Iteration",
                    status = "Undone", # Done, Undone
                    name = fake.bs(),
                    estimated_hours = None
                )
                inserted_task = repository.add_data_flush(task)
                
        repository.commit()

        stdout(inserted_proj.id)
        # repository.add_data(project)


service = Service()
