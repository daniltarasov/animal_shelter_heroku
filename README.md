Traceback (most recent call last):
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
psycopg2.errors.UndefinedTable: relation "p_library_author" does not exist
LINE 1: UPDATE "p_library_author" SET "full_name" = 'Николай Василье...
               ^
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "manage.py", line 23, in <module>
    main()
  File "manage.py", line 19, in main
    execute_from_command_line(sys.argv)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/base.py", line 330, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/base.py", line 371, in execute
    output = self.handle(*args, **options)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/commands/loaddata.py", line 72, in handle
    self.loaddata(fixture_labels)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/commands/loaddata.py", line 114, in loaddata
    self.load_label(fixture_label)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/management/commands/loaddata.py", line 181, in load_label
    obj.save(using=self.using)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/core/serializers/base.py", line 223, in save
    models.Model.save_base(self.object, using=using, raw=True, **kwargs)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/models/base.py", line 787, in save_base
    updated = self._save_table(
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/models/base.py", line 869, in _save_table
    updated = self._do_update(base_qs, using, pk_val, values, update_fields,
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/models/base.py", line 923, in _do_update
    return filtered._update(values) > 0
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/models/query.py", line 803, in _update
    return query.get_compiler(self.db).execute_sql(CURSOR)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1515, in execute_sql
    cursor = super().execute_sql(result_type)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1154, in execute_sql
    cursor.execute(sql, params)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/backends/utils.py", line 98, in execute
    return super().execute(sql, params)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/backends/utils.py", line 66, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/backends/utils.py", line 75, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/app/.heroku/python/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: Problem installing fixture '/app/data.json': Could not load p_library.Author(pk=1): relation "p_library_author" does not exist
LINE 1: UPDATE "p_library_author" SET "full_name" = 'Николай Василье...