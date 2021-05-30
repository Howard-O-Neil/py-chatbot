import enum

class BacklogStatus(enum.Enum):
  Done = 'Done'
  UnDone = 'UnDone'
  PartialDone = 'PartialDone'

class TaskType(enum.Enum):
  IterationTask = 'IterationTask',
  ProjectTask = 'ProjectTask'
