#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('playlistid')
        r.fieldcell('trackid')
        r.fieldcell('_multikey')

    def th_order(self):
        return 'playlistid'

    def th_query(self):
        return dict(column='_multikey', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('playlistid' )
        fb.field('trackid' )
        fb.field('_multikey' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
