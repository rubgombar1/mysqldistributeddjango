class principalRouter(object):
    """
    A router to control all database operations on models in
    the principal application
    """
    '''
    def db_for_read(self, model, **hints):
        """
        Point all operations on principal models to 'replica1'
        """
        if model._meta.app_label == 'principal':
            return 'replica1'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'principal':
            return 'default'
        return None
 
    def allow_migrate(self, db, model):
        """
        Make sure the 'principal' app only appears on the 'other' db
        """
        if db == 'replica1':
            return model._meta.app_label == 'principal'
        elif model._meta.app_label == 'principal':
            return False
        return None
    '''