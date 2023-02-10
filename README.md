
## Installation

Build and run the docker-compose file.
```shell
docker compose up -d --build
```

Enter the parent container and create a superuser.
```shell
docker compose exec -it parent bash
python manage.py createsuperuser
```

## Usage

Now, there will be 2 Django apps running on 2 ports: 8000 and 8001.

First app is the parent that provide authentication for the second app.

Second app uses custom [DB router](db_router.py), that written according to [this article](https://docs.djangoproject.com/en/4.1/topics/db/multi-db/#database-routers).


Open both admin panels and create / update some example model instances.

Changes will appear in both app's admin panels in `/admin/auditlog/logentry/` section.

But LogEntry changes won't be visible if these changes were made in different app.

It's because app doesn't contains other app's models and cannot retrieve `verbose_name` of field from other app.

So in this cases we can just skip `verbose_name` field and use field name instead.
