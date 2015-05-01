import pygal
#""" line graph"""
##line = pygal.Line()
#line = pygal.StackedLine(fill = True)
#line.title = "website hits in the past 2 years"
#line.x_labels = map(str, range(2012, 2014))
##line.add("Page views", [None, 0,12,32,72, 148])
#line.add("Site A", [None, 0, 12, 32, 72, 148])
#line.add("Site B", [2, 16, 12, 87, 91, 342])
#line.add("Site C", [42, 55,84, 88, 90, 171])
#line.render_to_file("linechart.svg")

#""" bar graph"""
##bar = pygal.Bar()
#bar = pygal.StackedBar()
##bar = pygal.HorizontalBar()
#bar.title = 'Searches for term: sleep'
#bar.x_labels = map(str, range(2011, 2015))
#bar.add("Men", (81,88, 98, 100))
#bar.add("Women", (78, 84, 69, 92))
#bar.render_to_file("bar_chart.svg")


##"""xy chart / scatter plot"""
##xy_chart = pygal.XY()
#xy_chart = pygal.XY(stroke = False)
#xy_chart.add("Value 1", [(-50, -30), (100, 45),(120,222)])
#xy_chart.add("Value 2", [(-2, -14), (370, 444)])
#xy_chart.render_to_file("xy_chart.svg")

#from datetime import datetime, timedelta
##date_Y = pygal.DateY()
#date_Y = pygal.DateY(x_label_rotation = 25)
#date_Y.title = ("Flight and amout of "
#                 "passengers arriving from "
#                 "St.Louis.")
#date_Y.add("Arrival", [(datetime(2014,1,5),42),
#                        (datetime(2014,1,14),123),
#                        (datetime(2014,2,2),97),
#                        (datetime(2014,3,22),164)])
#date_Y.render_to_file(u"datey_chart.svg")
