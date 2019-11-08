# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('media_types',legacy_name='main.media_types',legacy_db='chinook',pkey='mediatypeid',caption_field='name',name_long='media_types',name_plural='media_types')
        tbl.column('mediatypeid',dtype='I',name_long='Id',legacy_name='MediaTypeId')
        tbl.column('name',size='0:120',name_long='Name',legacy_name='Name')
