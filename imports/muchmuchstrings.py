#!/usr/bin/env python

from imports import globals


class banners:

    def print_license(self):
        print("")
        print(globals.vars.fulllicense)
        print("")

    def versionbanner(self):
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t\t    " + globals.vars.appname + ' v' + globals.vars.version)
        print("Built by:\t\t" + globals.vars.authors)
        print("Maintained by:\t\t" + ', '.join(globals.vars.maintainers))
        print("Is licensed under:\t" + globals.vars.licensev)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(globals.vars.fulllicense)
        print(globals.vars.usage)

    def print_available_payloads(self, array):
        answer = str(array[globals.vars.column_for_uid]) + "\t" + str(array[globals.vars.column_for_name]) + "\t" + str(array[globals.vars.column_for_version]) + "\t\t"
        answer += str(array[globals.vars.column_for_location]) + "\t\t" + str(array[globals.vars.colomn_for_time])
        print(answer)
