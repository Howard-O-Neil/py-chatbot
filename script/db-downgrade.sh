# arr=$(ls -ldA1 migrations/versions/* | awk '{print $9}' | grep -v '__pycache__')
current=$(python manage.py db show | grep 'Revision ID: ' | awk -F '[:]' '{print $2}' | xargs)
current="migrations/versions/${current}_.py"

python manage.py db downgrade
rm $current

# flag=0
# for i in $arr; do
#   if [ $i = $current ];
#   then 
#     python manage.py db downgrade
#     flag=1;
#   fi;

#   [ $flag -eq 1 ] && rm $i && flag=1
#   echo $flag
# done