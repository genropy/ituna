#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='ituna package',sqlschema='ituna',sqlprefix=True,
                    name_short='Ituna', name_long='Ituna music', name_full='Ituna')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
