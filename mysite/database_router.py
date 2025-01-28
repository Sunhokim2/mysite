class ServerStatusRouter:
    """
    - 'server_status' 앱의 모든 모델은 server_status 데이터베이스를 사용.
    - 나머지 앱의 모델은 기본 데이터베이스를 사용.
    """
    app_label_to_database = {
        'monitor': 'server_status',
    }

    def db_for_read(self, model, **hints):
        return self.app_label_to_database.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return self.app_label_to_database.get(model._meta.app_label, 'default')

    def allow_relation(self, obj1, obj2, **hints):
        db_set = {self.app_label_to_database.get(obj1._meta.app_label, 'default'),
                  self.app_label_to_database.get(obj2._meta.app_label, 'default')}
        return len(db_set) == 1 or 'default' in db_set

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == self.app_label_to_database.get(app_label, 'default')
