#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('albumid')
        r.fieldcell('title')
        r.fieldcell('artistid')

    def th_order(self):
        return 'albumid'

    def th_query(self):
        return dict(column='title', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('albumid')
        fb.field('title')
        fb.field('artistid')
        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@tracks')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
