#import pygal

##"""pie chart / stacked pie chart"""
#pie_chart = pygal.Pie()
#pie_chart.title = "Total top tablet sales in 2013 (in %)"
#pie_chart.add ("iPad & iPad mini", [19.7, 21.31,2])
#pie_chart.add ("Surface Pro 2", 36.3)
#pie_chart.add ("Surface 2", 24.5)
#pie_chart.add ("Nexus 7", 17.5)
#pie_chart.render_to_file("pie_chart.svg")

##"""radar chart"""
#radar_chart = pygal.Radar()
#radar_chart.title = "Prodct Budget Fighres"
#radar_chart.x_label = ["Sales", "Marketing", "Development",
#                       "Custom support", "Information Technology",
#                       "Administration"]
#radar_chart.add("Estimate", [40,20,100,20,30,20,10])
#radar_chart.add("Actual Spending", [70, 50, 40, 10, 17, 8, 10])
#radar_chart.render_to_file("radar_chart.svg")

##"""box plot : for comparing median"""
#box_plot = pygal.Box()
#box_plot.title = "Cost of Whole Milk in early 2014"
#box_plot.add("US Dollars", [2.08, 3.14, 3.89, 3.91, 3.94, 3.98])
#box_plot.add("Pound Sterling", [2.78, 3.84, 1.69, 4.71, 4.84, 4.92])
#box_plot.render_to_file("box_plot.svg")


##"""dot chart"""
#dot_chart = pygal.Dot(x_label_rotation=45)
#dot_chart.title = "Cost of Whole Milk in early 2014"
#dot_chart.x_labels = ["Jan", "Feb", "Mar", "Apr", "May", "June"]
#dot_chart.add("US Dollars", [2.08, 3.14, 3.89, 3.91, 3.94, 3.98])
#dot_chart.add("Pound Sterling", [2.78, 3.84, 1.69, 4.71, 4.84, 4.92])
#dot_chart.render_to_file("dot_chart.svg")

##"""funnel chart"""
#funnel_chart = pygal.Funnel(x_label_rotation=40)
#funnel_chart.title = "Amount of thrust used in a space shuttle at takeoff (in lbs)"
#funnel_chart.x_labels = ["pre-takeoff", "5 min", "10 min", "15 min",
#                         "20 min"]
#funnel_chart.add("Main Engine", [7000000, 615200, 5009600, 4347400, 2341211])
#funnel_chart.add("Engine #1", [1285000, 1072000, 89000, 51600, 12960])
#funnel_chart.add("Engine #3 & #4 (mid-size)", [990000, 61600, 21960, 18756, 11235])
#funnel_chart.render_to_file("funnel_chart.svg")

#"""gauge charts"""
##gauge_chart = pygal.Gauge()
#gauge_chart = pygal.Gauge(human_readable = True)
#gauge_chart.title = "Speed of space shuttle during takeoff"
#gauge_chart.x_labels = ["pre-takeoff", "5 min",
#                        "10 min", "15 min", "20 min"]
#gauge_chart.add("pre-takeoff", 0)
#gauge_chart.add("5 min", 96)
#gauge_chart.add("10 min", 167)
#gauge_chart.add("15 min", 249)
#gauge_chart.add("20 min", 339)
#gauge_chart.render_to_file("Gauge_chart.svg")
