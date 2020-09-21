
# https://chart-studio.plotly.com/~xijianlim/313/fb-prophets-times-series-forecast/#code
# import plotly.plotly as py
# from plotly.graph_objs import *
# py.sign_in('username', 'api_key')
# trace1 = {
#   "fill": None, 
#   "mode": "markers", 
#   "name": "actual no. of pageviews", 
#   "type": "scatter", 
#   "x": ["2010-01-01", "2010-02-01", "2010-03-01", "2010-04-01", "2010-05-01", "2010-06-01", "2010-07-01", "2010-08-01", "2010-09-01", "2010-10-01", "2010-11-01", "2010-12-01", "2011-01-01", "2011-02-01", "2011-03-01", "2011-04-01", "2011-05-01", "2011-06-01", "2011-07-01", "2011-08-01", "2011-09-01", "2011-10-01", "2011-11-01", "2011-12-01", "2012-01-01", "2012-02-01", "2012-03-01", "2012-04-01", "2012-05-01", "2012-06-01", "2012-07-01", "2012-08-01", "2012-09-01", "2012-10-01", "2012-11-01", "2012-12-01", "2013-01-01", "2013-02-01", "2013-03-01", "2013-04-01", "2013-05-01", "2013-06-01", "2013-07-01", "2013-08-01", "2013-09-01", "2013-10-01", "2013-11-01", "2013-12-01", "2014-01-01", "2014-02-01", "2014-03-01", "2014-04-01", "2014-05-01", "2014-06-01", "2014-07-01", "2014-08-01", "2014-09-01", "2014-10-01", "2014-11-01", "2014-12-01", "2015-01-01", "2015-02-01", "2015-03-01", "2015-04-01", "2015-05-01", "2015-06-01", "2015-07-01", "2015-08-01", "2015-09-01", "2015-10-01", "2015-11-01", "2015-12-01", "2016-01-01", "2016-02-01", "2016-03-01", "2016-04-01", "2016-05-01", "2016-06-01", "2016-07-01", "2016-08-01", "2016-09-01", "2016-10-01", "2016-11-01", "2016-12-01", "2017-01-01", "2017-02-01", "2017-03-01", "2017-04-01", "2017-05-01", "2017-06-01", "2017-07-01", "2017-08-01", "2017-08-31", "2017-09-30", "2017-10-31", "2017-11-30", "2017-12-31", "2018-01-31", "2018-02-28", "2018-03-31", "2018-04-30", "2018-05-31", "2018-06-30", "2018-07-31"], 
#   "y": [320886.9999999999, 314097.9999999998, 362072.0000000003, 236704.9999999998, 303236.00000000006, 423172.00000000023, 482914.00000000023, 398280.0, 386059.9999999997, 357998.9999999997, 309572.0000000001, 426793.00000000006, 429960.99999999994, 580674.0000000002, 627743.0000000002, 502376.0000000003, 476125.0000000001, 424530.0000000001, 374291.99999999994, 555780.9999999998, 587462.9999999999, 684769.9999999998, 592894.0000000002, 329485.99999999977, 394658.9999999999, 240326.0000000001, 249377.0000000001, 404163.0000000001, 549897.9999999998, 405974.0000000001, 361619.9999999999, 307308.9999999999, 282868.9999999999, 445801.9999999998, 389680.99999999994, 397827.0000000003, 549445.0000000001, 806969.0, 747679.9999999998, 585652.0, 709662.0000000002, 912874.9999999998, 670738.9999999997, 547182.0000000003, 431319.00000000006, 453948.00000000035, 403257.99999999994, 323602.0000000002, 377460.99999999977, 528173.0, 490156.00000000006, 467074.0000000002, 453496.00000000023, 415931.00000000035, 531341.0000000005, 542204.0000000001, 657162.0000000001, 615070.9999999999, 560307.0000000002, 585652.0, 1437428.0000000005, 640416.0000000003, 1135096.9999999995, 1043220.9999999998, 780265.9999999998, 900202.9999999999, 1345551.9999999998, 984385.0000000002, 878477.9999999994, 1189860.999999999, 1436522.999999999, 1225163.0000000007, 825524.9999999995, 698799.9999999995, 940031.0, 1183072.0000000002, 1248244.999999999, 784792.0000000007, 1272685.0000000012, 1516630.9999999988, 2102736.0, 1879608.9999999986, 1599908.000000001, 1684995.0000000002, 1305724.0000000002, 1295767.0000000002, 1493096.0000000012, 1503505.9999999988, 1346457.0, 1474539.9999999993, 1478160.9999999995, 2240324.000000001, "", "", "", "", "", "", "", "", "", "", "", ""]
# }
# trace2 = {
#   "fill": "tonexty", 
#   "line": {"color": "#57b8ff"}, 
#   "mode": "lines", 
#   "name": "upper_band", 
#   "type": "scatter", 
#   "x": ["2010-01-01", "2010-02-01", "2010-03-01", "2010-04-01", "2010-05-01", "2010-06-01", "2010-07-01", "2010-08-01", "2010-09-01", "2010-10-01", "2010-11-01", "2010-12-01", "2011-01-01", "2011-02-01", "2011-03-01", "2011-04-01", "2011-05-01", "2011-06-01", "2011-07-01", "2011-08-01", "2011-09-01", "2011-10-01", "2011-11-01", "2011-12-01", "2012-01-01", "2012-02-01", "2012-03-01", "2012-04-01", "2012-05-01", "2012-06-01", "2012-07-01", "2012-08-01", "2012-09-01", "2012-10-01", "2012-11-01", "2012-12-01", "2013-01-01", "2013-02-01", "2013-03-01", "2013-04-01", "2013-05-01", "2013-06-01", "2013-07-01", "2013-08-01", "2013-09-01", "2013-10-01", "2013-11-01", "2013-12-01", "2014-01-01", "2014-02-01", "2014-03-01", "2014-04-01", "2014-05-01", "2014-06-01", "2014-07-01", "2014-08-01", "2014-09-01", "2014-10-01", "2014-11-01", "2014-12-01", "2015-01-01", "2015-02-01", "2015-03-01", "2015-04-01", "2015-05-01", "2015-06-01", "2015-07-01", "2015-08-01", "2015-09-01", "2015-10-01", "2015-11-01", "2015-12-01", "2016-01-01", "2016-02-01", "2016-03-01", "2016-04-01", "2016-05-01", "2016-06-01", "2016-07-01", "2016-08-01", "2016-09-01", "2016-10-01", "2016-11-01", "2016-12-01", "2017-01-01", "2017-02-01", "2017-03-01", "2017-04-01", "2017-05-01", "2017-06-01", "2017-07-01", "2017-08-01", "2017-08-31", "2017-09-30", "2017-10-31", "2017-11-30", "2017-12-31", "2018-01-31", "2018-02-28", "2018-03-31", "2018-04-30", "2018-05-31", "2018-06-30", "2018-07-31"], 
#   "y": [405946.0375705701, 414645.5103473563, 467989.7827873357, 427697.5247519792, 433260.88605640724, 426435.71015726053, 491557.7476173895, 490659.9607353202, 469387.284979207, 526050.7025860759, 499556.32280528673, 449844.3284628506, 543509.0413209733, 473700.3400815173, 771104.8421833123, 576955.7288616891, 544595.3684344367, 562163.0006660154, 674068.0654430864, 648911.9305502229, 605425.2354862054, 701441.2108763618, 695678.5578927941, 607858.4462274908, 700863.7799996197, 501352.5889695552, 578116.4899862335, 736462.3938846056, 844342.9293618585, 761139.7198157494, 792318.5916205643, 885004.1948593154, 831427.9413966784, 857858.1798694023, 748697.9759624328, 724976.4526455671, 914361.0534134732, 1113177.9444629347, 863186.5573084464, 936989.2735812194, 988816.8133468992, 964409.9450998557, 1040107.3134009237, 1093031.8987974504, 993918.1752554826, 1136839.433278261, 970228.3590521519, 945222.2745939726, 1085619.1009648263, 1156727.5113860446, 1292798.000091921, 1145116.5802187936, 1174174.0013818943, 1148946.9861054525, 1265010.1871499792, 1282431.772545562, 1180614.5440086294, 1301271.6793428403, 1210181.5562370836, 1149248.6391396627, 1315599.1034205845, 1131476.7753815795, 1870318.9600743656, 1372203.4842075002, 1365093.8115303381, 1378373.1663916288, 1589750.340451879, 1475444.2282099717, 1388572.6130811835, 1571559.0683507598, 1570352.4489804942, 1352142.178605549, 1504413.9161784395, 1109495.9177679576, 1275948.5543107733, 1544479.1616100853, 1759163.1689838518, 1600926.1983058215, 1687034.3893103274, 1811528.6613178018, 1698825.6672184316, 1764645.0284534364, 1500442.2387604471, 1442697.444870031, 1746741.7005592259, 2139491.822704838, 1746887.9815860721, 1780210.6728283002, 1932026.138648465, 1881715.713428744, 1904610.9659262, 2017261.9941365407, 1637955.5122607837, 2081258.7719791855, 2076213.9347768172, 1815647.3755323454, 1859943.3717387444, 960027.8559286771, 4710151.991344921, 2040023.4060240313, 1605583.0773983647, 1924571.9682585762, 2291033.3942565867, 2080002.9225031578]
# }
# trace3 = {
#   "fill": "tonexty", 
#   "line": {"color": "#57b8ff"}, 
#   "mode": "lines", 
#   "name": "lower_band", 
#   "type": "scatter", 
#   "x": ["2010-01-01", "2010-02-01", "2010-03-01", "2010-04-01", "2010-05-01", "2010-06-01", "2010-07-01", "2010-08-01", "2010-09-01", "2010-10-01", "2010-11-01", "2010-12-01", "2011-01-01", "2011-02-01", "2011-03-01", "2011-04-01", "2011-05-01", "2011-06-01", "2011-07-01", "2011-08-01", "2011-09-01", "2011-10-01", "2011-11-01", "2011-12-01", "2012-01-01", "2012-02-01", "2012-03-01", "2012-04-01", "2012-05-01", "2012-06-01", "2012-07-01", "2012-08-01", "2012-09-01", "2012-10-01", "2012-11-01", "2012-12-01", "2013-01-01", "2013-02-01", "2013-03-01", "2013-04-01", "2013-05-01", "2013-06-01", "2013-07-01", "2013-08-01", "2013-09-01", "2013-10-01", "2013-11-01", "2013-12-01", "2014-01-01", "2014-02-01", "2014-03-01", "2014-04-01", "2014-05-01", "2014-06-01", "2014-07-01", "2014-08-01", "2014-09-01", "2014-10-01", "2014-11-01", "2014-12-01", "2015-01-01", "2015-02-01", "2015-03-01", "2015-04-01", "2015-05-01", "2015-06-01", "2015-07-01", "2015-08-01", "2015-09-01", "2015-10-01", "2015-11-01", "2015-12-01", "2016-01-01", "2016-02-01", "2016-03-01", "2016-04-01", "2016-05-01", "2016-06-01", "2016-07-01", "2016-08-01", "2016-09-01", "2016-10-01", "2016-11-01", "2016-12-01", "2017-01-01", "2017-02-01", "2017-03-01", "2017-04-01", "2017-05-01", "2017-06-01", "2017-07-01", "2017-08-01", "2017-08-31", "2017-09-30", "2017-10-31", "2017-11-30", "2017-12-31", "2018-01-31", "2018-02-28", "2018-03-31", "2018-04-30", "2018-05-31", "2018-06-30", "2018-07-31"], 
#   "y": [169843.91939418306, 174978.7535703093, 198100.02934391008, 184385.09676354914, 179914.1397594088, 184112.51082345, 205721.47540724074, 214572.3366678815, 200642.3985949453, 228359.35798436246, 207762.91115702153, 199425.52236567816, 225560.25042097556, 195934.56873085798, 333791.02694116725, 250464.35002981313, 238216.119361434, 249247.6573251178, 277893.62043640803, 281864.40780241234, 256025.4430921037, 296661.61456536053, 290808.8818076463, 273450.5688884212, 302820.01170440356, 218570.07659485575, 255437.07545671702, 318364.08741504577, 360027.38061122876, 332306.1444753831, 343609.9539451412, 373878.0694620554, 365525.7034096639, 376379.98551403836, 326447.10065339296, 303680.98174270143, 375861.393896965, 475179.96848874434, 375120.36029718537, 402908.673663011, 424609.331784669, 413075.23396054556, 447994.8363111144, 463610.2174009672, 438663.52343448513, 465873.8222667221, 429866.5009647069, 388508.7564402943, 475432.8398377099, 497701.66813218396, 554578.4077792844, 502299.2709261947, 500629.49988786463, 492362.6837699229, 546984.8646733967, 559469.163178659, 514667.7408205045, 569617.8950166747, 530364.6365422037, 467863.71526115196, 571657.2701324294, 495357.11953775113, 782101.2991820414, 591818.8078138157, 563849.8892186425, 593415.301313016, 651350.2487017917, 650433.0769721426, 578207.5605162383, 665913.693999919, 675175.1644234776, 579140.5734337857, 651115.4324254459, 467622.03454475675, 535999.5742386949, 657049.8755631438, 742337.8118642879, 688898.2302026099, 721963.8393059124, 746643.395403358, 720063.2630882963, 759975.0709150309, 639863.2815885136, 603942.1077334184, 745999.866118433, 922821.1894998613, 731750.1528739657, 756474.2002977816, 792010.7271760125, 759666.975575003, 828826.5648841613, 875147.8220330734, 710600.3722112012, 852730.6331934849, 884631.5078179598, 764463.1790337642, 783663.0986625848, 411145.00336454407, 1944943.9622717085, 862257.0283097372, 686723.2553272512, 793130.2068522094, 988735.7946901983, 873856.1912180546]
# }
# trace4 = {
#   "line": {"color": "##ff6d22"}, 
#   "mode": "lines", 
#   "name": "model line of best fit", 
#   "type": "scatter", 
#   "x": ["2010-01-01", "2010-02-01", "2010-03-01", "2010-04-01", "2010-05-01", "2010-06-01", "2010-07-01", "2010-08-01", "2010-09-01", "2010-10-01", "2010-11-01", "2010-12-01", "2011-01-01", "2011-02-01", "2011-03-01", "2011-04-01", "2011-05-01", "2011-06-01", "2011-07-01", "2011-08-01", "2011-09-01", "2011-10-01", "2011-11-01", "2011-12-01", "2012-01-01", "2012-02-01", "2012-03-01", "2012-04-01", "2012-05-01", "2012-06-01", "2012-07-01", "2012-08-01", "2012-09-01", "2012-10-01", "2012-11-01", "2012-12-01", "2013-01-01", "2013-02-01", "2013-03-01", "2013-04-01", "2013-05-01", "2013-06-01", "2013-07-01", "2013-08-01", "2013-09-01", "2013-10-01", "2013-11-01", "2013-12-01", "2014-01-01", "2014-02-01", "2014-03-01", "2014-04-01", "2014-05-01", "2014-06-01", "2014-07-01", "2014-08-01", "2014-09-01", "2014-10-01", "2014-11-01", "2014-12-01", "2015-01-01", "2015-02-01", "2015-03-01", "2015-04-01", "2015-05-01", "2015-06-01", "2015-07-01", "2015-08-01", "2015-09-01", "2015-10-01", "2015-11-01", "2015-12-01", "2016-01-01", "2016-02-01", "2016-03-01", "2016-04-01", "2016-05-01", "2016-06-01", "2016-07-01", "2016-08-01", "2016-09-01", "2016-10-01", "2016-11-01", "2016-12-01", "2017-01-01", "2017-02-01", "2017-03-01", "2017-04-01", "2017-05-01", "2017-06-01", "2017-07-01", "2017-08-01", "2017-08-31", "2017-09-30", "2017-10-31", "2017-11-30", "2017-12-31", "2018-01-31", "2018-02-28", "2018-03-31", "2018-04-30", "2018-05-31", "2018-06-30", "2018-07-31"], 
#   "y": [256966.18832921924, 265679.0826393773, 307834.36125371733, 276498.9264399858, 280958.64991286106, 284464.4557435253, 318543.65945237916, 322013.7457145281, 302733.02456271707, 343424.20029548736, 322568.41869865626, 298672.5346698406, 349619.16642039886, 303671.5167360481, 501501.54285774566, 378986.62163547706, 360480.9939154471, 380697.1286475323, 436675.79804701265, 426072.29100007174, 393558.6439718203, 463312.8554070448, 448600.0481163358, 403422.3323525062, 455807.4399933109, 334188.36202457774, 387721.6996717333, 478891.81035315944, 550888.1572170056, 507940.8861559206, 534081.2955151311, 571206.1148877215, 550581.6527642055, 573498.4038726204, 498774.56750989985, 481269.9068964203, 595192.616731169, 725992.2028271108, 583176.0358165667, 611790.4780101163, 656936.7020819288, 630372.9573603349, 680184.7450235642, 703111.7068381691, 664980.3164310586, 718499.4556730235, 645894.0233531959, 607524.3601122618, 727117.9110449621, 742500.2354871844, 850796.1598338771, 754909.5626355805, 758140.6569015855, 758428.6352921738, 839547.7881840619, 838720.3001598989, 779315.355327599, 874181.437863334, 811691.3680420779, 743304.3568420731, 860306.2276975325, 738912.7661267866, 1208098.6505201897, 902964.5736822968, 849851.3544836207, 887861.6062836405, 1007915.3660053166, 973064.4788503054, 889418.1535410236, 1036570.5603589272, 993367.7767912421, 884552.7241968462, 989370.9459028989, 718170.321712663, 825533.8042433014, 1009709.0021931536, 1150656.1805643989, 1050814.2889664448, 1094780.3966047019, 1159922.997001366, 1107689.8478456542, 1143563.5798529321, 985547.4229751197, 942704.3074928323, 1155509.9464747913, 1397075.8455245083, 1113438.9036090025, 1158034.7935632777, 1233262.0045150334, 1173447.6570985818, 1255986.6454738642, 1287650.5138976302, 1084405.7555609103, 1366976.5951035873, 1391908.7510248134, 1167682.5464390703, 1217537.4591476384, 640639.2045462753, 3036158.7063274398, 1325261.7556258726, 1040172.5703573936, 1249784.0873590428, 1526174.2845933265, 1329353.3410443012]
# }
# data = Data([trace1, trace2, trace3, trace4])
# layout = {
#   "title": "FB- Prophet's Times Series Forecast", 
#   "xaxis": {
#     "title": "Monthly Dates", 
#     "ticklen": 5, 
#     "gridcolor": "rgb(255, 255, 255)", 
#     "gridwidth": 2, 
#     "zerolinewidth": 1
#   }, 
#   "yaxis": {
#     "title": "Pageviews", 
#     "ticklen": 5, 
#     "gridcolor": "rgb(255, 255, 255)", 
#     "gridwidth": 2, 
#     "zerolinewidth": 1
#   }, 
#   "plot_bgcolor": "rgb(243, 243, 243)", 
#   "paper_bgcolor": "rgb(243, 243, 243)"
# }
# fig = Figure(data=data, layout=layout)
# plot_url = py.plot(fig)