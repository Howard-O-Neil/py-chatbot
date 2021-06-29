sudo apt install grc
pip install virtualenv
pip install --upgrade virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirement.txt
docker rm -f docker-proxy-dns
docker-compose -f docker-proxy-dns.yaml up -d | true
docker-compose -f docker-proxy-dns.yaml restart | true
docker restart docker-proxy-dns | true

touch gunicorn.error.log
touch gunicorn.log

echo "\n=== This script has been executed without errors ==="
echo "Please run below command"
echo "source venv/bin/activate       (bash shell)"
echo ". venv/bin/activate            (sh shell)"
echo "source venv/bin/activate.fish  (fish shell)"
echo "venv/bin/activate.ps1          (window powershell)"