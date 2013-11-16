!/usr/bin/env bash
export MEMCACHE_SERVERS='' MEMCACHIER_SERVERS=''

if [ -f bin/run_collectstatic ]; then
    echo "-----> Collecting Static"
    python manage.py collectstatic --noinput --settings=envs.live_local
    python manage.py collectstatic --noinput --settings=envs.live

fi

if [ -f bin/run_compress ]; then
    echo "-----> Compress"
    python manage.py compress --settings=envs.live
fi

if [ -f bin/run_syncstatic ]; then
    echo "-----> Sync to S3"
    python manage.py sync_static --gzip --expires --settings=envs.live
fi

echo "-----> Post-compile done"