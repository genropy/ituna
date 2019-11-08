# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('artists',legacy_name='main.artists',legacy_db='chinook',pkey='artistid',caption_field='name',name_long='Artist',name_plural='Artists')
        tbl.column('artistid',dtype='I',name_long='Id',legacy_name='ArtistId')
        tbl.column('name',size='0:120',name_long='Name',legacy_name='Name')
