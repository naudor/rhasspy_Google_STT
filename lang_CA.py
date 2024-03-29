# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, print_function, unicode_literals

import math

from .lang_EU import Num2Word_EU


class Num2Word_CA(Num2Word_EU):
    CURRENCY_FORMS = {
        'EUR': (('euro', 'euros'), ('céntim', 'céntims')),
        'ESP': (('pesseta', 'pessetes'), ('céntim', 'céntims')),
        'USD': (('dolar', 'dólars'), ('céntim', 'céntims')),
        'PEN': (('sol', 'sols'), ('céntim', 'céntims')),
    }

    # //CHECK: Is this sufficient??
    GIGA_SUFFIX = None
    MEGA_SUFFIX = "illó"

    def setup(self):
        lows = ["cuatr", "tr", "b", "m"]
        self.high_numwords = self.gen_high_numwords([], [], lows)
        self.negword = "menys "
        self.pointword = "punt"
        self.errmsg_nonnum = "Només nombres poden ser convertits a paraules."
        self.errmsg_toobig = (
            "Nombre molt gran per ser convertit a paraules."
            )
        self.gender_stem = ""
        self.exclude_title = ["i", "menys", "punt"]
        self.mid_numwords = [(1000, "mil"), (100, "cent"), (90, "noranta"),
                             (80, "vuitanta"), (70, "setanta"), (60, "seixanta"),
                             (50, "cinquanta"), (40, "quaranta"),
                             (30, "trenta")]
        self.low_numwords = [	"vint-i-nou", "vint-i-vuit", "vint-i-set",
				"vint-i-sis", "vint-i-cinc", "vint-i-quatre",
				"vint-i-tres", "vint-i-dos", "vint-i-un",
				"vint", "dinou", "divuit", "disset",
				"setze", "quinze", "catorze", "tretze", "dotze",
				"onze", "deu", "nou", "vuit", "set", "sis",
				"cinc", "quatre", "tres", "dos", "un", "zero"]
        self.ords = {1: "primer",
                     2: "segon",
                     3: "tercer",
                     4: "cuart",
                     5: "cinquè",
                     6: "sisè",
                     7: "setè",
                     8: "vuitè",
                     9: "novè",
                     10: "décim",
                     20: "vigésim",
                     30: "trigésim",
                     40: "quadragésim",
                     50: "quincuagésim",
                     60: "sexagésim",
                     70: "septuagésim",
                     80: "octogésim",
                     90: "nonagésim",
                     100: "centésim",
                     200: "ducentésim",
                     300: "tricentésim",
                     400: "cuadrigentésim",
                     500: "quingentésim",
                     600: "sexcentésim",
                     700: "septigentésim",
                     800: "octigentésim",
                     900: "noningentésim",
                     1e3: "milésim",
                     1e6: "millonésim",
                     1e9: "billonésim",
                     1e12: "trillonésim",
                     1e15: "cuadrillonésim"}

    def merge(self, curr, next):
        ctext, cnum, ntext, nnum = curr + next

        if cnum == 1:
            if nnum < 1000000:
                return next
            ctext = "un"
        elif cnum == 100 and not nnum % 1000 == 0:
            ctext += "t" + self.gender_stem

        if nnum < cnum:
            if cnum < 100:
                return "%s y %s" % (ctext, ntext), cnum + nnum
            return "%s %s" % (ctext, ntext), cnum + nnum
        elif (not nnum % 1000000) and cnum > 1:
            ntext = ntext[:-3] + "lons"

        if nnum == 100:
            if cnum == 5:
                ctext = "cinc"
                ntext = ""
            elif cnum == 7:
                ctext = "set"
            elif cnum == 9:
                ctext = "nou"
            ntext += "-cent" + self.gender_stem + "s"
        else:
            ntext = " " + ntext

        return (ctext + ntext, cnum * nnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        if value == 0:
            text = ""
        elif value <= 10:
            text = "%s%s" % (self.ords[value], self.gender_stem)
        elif value <= 12:
            text = (
                "%s%s%s" % (self.ords[10], self.gender_stem,
                            self.to_ordinal(value - 10))
                    )
        elif value <= 100:
            dec = (value // 10) * 10
            text = (
                "%s%s %s" % (self.ords[dec], self.gender_stem,
                             self.to_ordinal(value - dec))
                    )
        elif value <= 1e3:
            cen = (value // 100) * 100
            text = (
                "%s%s %s" % (self.ords[cen], self.gender_stem,
                             self.to_ordinal(value - cen))
                    )
        elif value < 1e18:
            # Round down to the nearest 1e(3n)
            # dec contains the following:
            # [ 1e3,  1e6): 1e3
            # [ 1e6,  1e9): 1e6
            # [ 1e9, 1e12): 1e9
            # [1e12, 1e15): 1e12
            # [1e15, 1e18): 1e15
            dec = 1000 ** int(math.log(int(value), 1000))

            # Split the parts before and after the word for 'dec'
            # eg (12, 345) = divmod(12_345, 1_000)
            high_part, low_part = divmod(value, dec)

            cardinal = self.to_cardinal(high_part) if high_part != 1 else ""
            text = (
                "%s%s%s %s" % (cardinal, self.ords[dec], self.gender_stem,
                               self.to_ordinal(low_part))
                    )
        else:
            text = self.to_cardinal(value)
        return text.strip()

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, "º" if self.gender_stem == '' else "ª")

    def to_currency(self, val, currency='EUR', cents=True, separator=' amb',
                    adjective=False):
        result = super(Num2Word_CA, self).to_currency(
            val, currency=currency, cents=cents, separator=separator,
            adjective=adjective)
        # Handle exception, in spanish is "un euro" and not "uno euro"
        return result
