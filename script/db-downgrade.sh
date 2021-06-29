# arr=$(ls -ldA1 migrations/versions/* | awk '{print $9}' | grep -v '__pycache__')
current=$(flask db show | grep 'Revision ID: ' | awk -F '[:]' '{print $2}' | xargs)
current="migrations/versions/${current}_.py"

flask db downgrade
rm $current

# flag=0
# for i in $arr; do
#   if [ $i = $current ];
#   then 
#     flask db downgrade
#     flag=1;
#   fi;

#   [ $flag -eq 1 ] && rm $i && flag=1
#   echo $flag
# done