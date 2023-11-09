class PostRouter():
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'Post':
            return 'DBPost'
        return None
    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'Post':
            return "DBPost"
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'Post' or obj2._meta.db_table == 'Post':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'sun_blog':
            return db == 'DBPost'
        return None