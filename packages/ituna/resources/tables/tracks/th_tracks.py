#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('trackid')
        r.fieldcell('name')
        r.fieldcell('albumid')
        r.fieldcell('mediatypeid')
        r.fieldcell('genreid')
        r.fieldcell('composer')
        r.fieldcell('milliseconds')
        r.fieldcell('bytes')
        r.fieldcell('unitprice')

    def th_order(self):
        return 'trackid'

    def th_query(self):
        return dict(column='name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('trackid')
        fb.field('name')
        fb.field('albumid')
        fb.field('mediatypeid')
        fb.field('genreid')
        fb.field('composer')
        fb.field('milliseconds')
        fb.field('bytes')
        fb.field('unitprice')
        pane = bc.contentPane(region='center',margin='2px')
        pane.dialogTableHandler(relation='@playlists')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
