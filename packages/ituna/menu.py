#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    ituna = root.branch('Ituna music')
    ituna.thpage('Artists',table='ituna.artists')
    ituna.thpage('Customers',table='ituna.customers')
    ituna.thpage('Employees',table='ituna.employees')
    ituna.thpage('Genres',table='ituna.genres')
    ituna.thpage('Albums',table='ituna.albums')
    ituna.thpage('Tracks',table='ituna.tracks')
    ituna.thpage('Invoices',table='ituna.invoices')
    ituna.thpage('Invoice items',table='ituna.invoice_items')
    ituna.thpage('Media_types',table='ituna.media_types')
    #ituna.thpage('playlist_track',table='ituna.playlist_track')
    ituna.thpage('Playlists',table='ituna.playlists')
    