#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:40:37 2020

@author: nooryoussef

Plot correlation between dN^h/dS^h and WCN and RSA 
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

RstPath = '../Results/'

#RSA#
rsa_dict = {'1qhw' : [0.638709677, 0.156976744, 0.049751244, 0.186131387, 0, 0, 0, 0.017241379, 0, 0, 0.003508772, 0, 0, 0.166666667, 0.352201258, 0.574358974, 0.511627907, 0.490566038, 0.091666667, 0.267857143, 0.180232558, 0.604651163, 0.233576642, 0.004484305, 0.28125, 0.15503876, 0.015384615, 0.03875969, 0.508474576, 0.098654709, 0.015228426, 0, 0.430656934, 0.075581395, 0.086206897, 0.537777778, 0.664974619, 0.392857143, 0.173076923, 0.131782946, 0.362694301, 0.008333333, 0.005076142, 0, 0, 0, 0, 0.010362694, 0, 0, 0.007604563, 0.379166667, 0.476744186, 0.038461538, 0, 0.633928571, 0.32642487, 0.147286822, 0.671794872, 0.046632124, 0.529661017, 0.058394161, 0, 0.306666667, 0.30941704, 0, 0, 0.147982063, 0.471502591, 0.034482759, 0.016666667, 0.322580645, 0.352331606, 0.821167883, 0.209302326, 0.004975124, 0.47810219, 0.805128205, 0.076142132, 0.251572327, 0.003508772, 0.182509506, 0, 0, 0.007751938, 0, 0.020512821, 0.129464286, 0, 0.209821429, 0.353233831, 0.307692308, 0.312820513, 0.195402299, 0.516129032, 0.03875969, 0.004444444, 0.192893401, 0.255813953, 0.015209125, 0.193548387, 0.779661017, 0.472081218, 0.083870968, 0.860169492, 0.098540146, 0, 0.251282051, 0.008333333, 0.503144654, 0.258064516, 0.257861635, 0.182509506, 0.060836502, 0.379562044, 0.104477612, 0.394160584, 0.15, 0.61440678, 0.005747126, 0.41509434, 0.890510949, 0.212903226, 0.78974359, 0.005076142, 0.162790698, 0, 0, 0, 0, 0, 0.004975124, 0.015544041, 0, 0.068965517, 0.174107143, 0.039800995, 0, 0.048076923, 0.046153846, 0.012903226, 0.321243523, 0.492227979, 0.154166667, 0.833333333, 0.438709677, 0.36, 0.208888889, 0.050314465, 0.520179372, 0.526785714, 0.289308176, 0.781021898, 0.430051813, 0.696517413, 0.346153846, 0.316091954, 0.054263566, 0.572992701, 0.470930233, 0.004444444, 0.2039801, 0.180645161, 0.203508772, 0.004975124, 0.457627119, 0.63559322, 0.244444444, 0.014925373, 0.465116279, 0.472868217, 0.085271318, 0.733050847, 0.107623318, 0.21761658, 0, 0, 0.004975124, 0, 0, 0, 0, 0, 0, 0.005076142, 0.080701754, 0, 0.015228426, 0, 0.062780269, 0.200892857, 0, 0.13836478, 0.023255814, 0.642335766, 0.125748503, 0.009950249, 0.132183908, 0.504237288, 0.461538462, 0.004975124, 0.343065693, 0.383647799, 0.134328358, 0, 0.333333333, 0.581395349, 0.243346008, 0.317307692, 0.028735632, 0.081395349, 0, 0.003802281, 0.024875622, 0.023952096, 0, 0.035714286, 0, 0.147321429, 0, 0.004975124, 0, 0, 0.004975124, 0.168888889, 0.046632124, 0.605381166, 0.558974359, 0.394230769, 0.028735632, 0, 0.019011407, 0.011494253, 0.004975124, 0, 0, 0, 0.009615385, 0.01025641, 0.241666667, 0.066964286, 0.279792746, 0.41509434, 0.129032258, 0.32183908, 0.620437956, 0.178571429, 0.368888889, 0.737226277, 0.610169492, 0.034482759, 0.289308176, 0.820512821, 0.567307692, 0.087452471, 0.353233831, 0.423357664, 0.1125, 0.209821429, 0.25095057, 0.048076923, 0.277419355, 0.538116592, 0.715025907, 0.032258065, 0.36318408, 0.009615385, 0, 0, 0.005813953, 0.038022814, 0.017241379, 0.251121076, 0, 0.057692308, 0.419354839, 0.686440678, 0.233183857, 0.013392857, 0.032258065, 0.010152284, 0.11627907, 0, 0.045977011, 0.044843049, 0.054263566, 0.535483871, 0.336538462, 0.495762712, 0.541935484, 0.258706468, 0.229166667, 0.478813559, 0.197674419, 0.380645161, 0.029850746, 0.635220126, 0.441605839, 0.182481752, 1.106918239], 
       '1pek':[0.240310078, 0.457364341, 0.124444444, 0.63372093, 0.702564103, 0.07751938, 0.144654088, 0.164912281, 0.009615385, 0.004975124, 0, 0.010948905, 0, 0.058064516, 0.096774194, 0.488372093, 0.335483871, 0.339622642, 0.759615385, 0.302325581, 0.393548387, 0.11627907, 0, 0.399239544, 0.136882129, 0.238341969, 0.408071749, 0.174193548, 0.007751938, 0, 0.457777778, 0.269230769, 0.006451613, 0.011976048, 0, 0, 0.005747126, 0, 0.005181347, 0, 0, 0.020304569, 0.183856502, 0.217054264, 0.64516129, 0.035714286, 0.603773585, 0.098654709, 0, 0.452914798, 0.625, 0.113138686, 0.03875969, 0.284444444, 0.169642857, 0.166666667, 0.300847458, 0.191860465, 0.247148289, 0.239543726, 0.882129278, 0.238709677, 0.335483871, 0.547445255, 0.025906736, 0.317307692, 0.220512821, 0, 0.004464286, 0, 0, 0, 0, 0, 0, 0.005813953, 0, 0, 0, 0.496350365, 0.174418605, 0.129277567, 0, 0, 0, 0.063559322, 0.381355932, 0, 0.253333333, 0, 0.029166667, 0, 0, 0.004237288, 0, 0, 0.196891192, 0.32642487, 0.712820513, 0.038461538, 0.348387097, 0.25, 0.213333333, 0.216730038, 0.541935484, 0.209302326, 0.005076142, 0.152284264, 0.271317829, 0, 0, 0.305699482, 0.191666667, 0, 0.139534884, 0.490322581, 0.041450777, 0.131355932, 0.594871795, 0.574358974, 0.288321168, 0.748717949, 0.119760479, 0.603773585, 0.402542373, 0.163461538, 0.068965517, 0, 0, 0.006451613, 0, 0.006451613, 0.009950249, 0.009615385, 0.009615385, 0.278846154, 0.490494297, 0.141935484, 0.490322581, 0.438709677, 0, 0.030769231, 0.316129032, 0, 0, 0.178294574, 0.364963504, 0, 0.097777778, 0.619354839, 0.290322581, 0.355769231, 0, 0.004464286, 0, 0, 0, 0, 0, 0, 0.18974359, 0.394871795, 0.4, 0.209302326, 0.295336788, 0, 0.200729927, 0.533333333, 0.178707224, 0, 0, 0, 0.077419355, 0.143497758, 0.578616352, 0.374193548, 0.017241379, 0.005988024, 0, 0, 0, 0, 0, 0.088082902, 0.310218978, 0.558935361, 0.056994819, 0.401459854, 0.058394161, 0, 0.6, 0.170833333, 0, 0, 0.224334601, 0.028846154, 0.625806452, 0.137931034, 0.009950249, 0.238341969, 0, 0, 0, 0, 0, 0.162790698, 0.232258065, 0.020304569, 0.288557214, 0, 0, 0.073684211, 0.218274112, 0.663461538, 0.336538462, 0.329032258, 0.337209302, 0.423357664, 0.419354839, 0.101522843, 0.258064516, 0.009615385, 0, 0, 0, 0, 0, 0, 0.013392857, 0.005747126, 0, 0, 0, 0, 0, 0.015209125, 0.019900498, 0.049107143, 0.063953488, 0.263681592, 0.596153846, 0.516949153, 0.093023256, 0.453488372, 0.085271318, 0.635658915, 0.232258065, 0, 0.113772455, 0.45620438, 0.152091255, 0, 0.147286822, 0.461139896, 0.180232558, 0.031007752, 0.066666667, 0.491525424, 0.538461538, 0.300518135, 0.034825871, 0.406451613, 0.471794872, 0.177664975, 0.238993711, 0.925, 0.490384615, 0.075581395, 0.275862069, 0.194871795, 0.129353234, 0, 0, 0.133079848, 0.041025641, 0.379487179, 0.205323194, 0.373333333, 0.945736434], 
       '2ppn' : [0.509615385, 0.120689655, 0.591111111, 0.229885057, 0.502242152, 0.470930233, 0.47715736, 0.24516129, 0.710691824, 0.230769231, 0.388601036, 0.471153846, 0.788321168, 0.36627907, 0.366666667, 0.100628931, 0.656779661, 0.671532847, 0.403846154, 0.266666667, 0.203488372, 0, 0.022988506, 0, 0.169642857, 0.034220532, 0.063953488, 0, 0.165178571, 0.169154229, 0.556053812, 0.549222798, 0.423076923, 0.597457627, 0.415254237, 0.233333333, 0.29015544, 0.025806452, 0, 0.182481752, 0.554404145, 0.445255474, 0.717948718, 0.627118644, 0.327044025, 0.254166667, 0.533898305, 0.008333333, 0.34375, 0.054726368, 0.173076923, 0.529661017, 0.688888889, 0.399103139, 0.143678161, 0.116751269, 0.47080292, 0, 0.028070175, 0.071748879, 0.33632287, 0, 0, 0.286821705, 0.466666667, 0, 0.019354839, 0.206896552, 0.307692308, 0.075555556, 0.270072993, 0, 0.309322034, 0, 0.168604651, 0, 0.225806452, 0.113207547, 0.694300518, 0.171102662, 0.162790698, 0.357414449, 0.211538462, 0.480620155, 0.622093023, 0.105769231, 0.464285714, 0.704402516, 0.817307692, 0.461928934, 0.020304569, 0.371069182, 0.503144654, 0.553571429, 0.03875969, 0.244186047, 0, 0.195402299, 0.025, 0.155440415, 0, 0.255605381, 0, 0.268656716, 0.411016949, 0.174129353, 0.578475336]}

#WCN# 
wcn_dict = {'1qhw':  [0.722389424, 0.997903716, 1.13432103, 1.241156198, 1.367844456, 1.449544289, 1.540450086, 1.593634803, 1.690446579, 1.580801134, 1.520864822, 1.454281975, 1.300389706, 1.093440822, 0.929250028, 0.785753936, 0.811516723, 0.84348275, 1.080962637, 1.148114577, 1.063432418, 0.961270876, 1.221699975, 1.352268564, 1.168007158, 1.159505865, 1.379038234, 1.297011636, 1.114057471, 1.197612576, 1.296528719, 1.167848407, 1.020282979, 1.128487648, 1.16129093, 0.911606526, 0.838798615, 0.930720313, 1.010172049, 1.161784782, 1.094177031, 1.271434345, 1.409638087, 1.489315927, 1.556952326, 1.656133358, 1.650409606, 1.549958497, 1.475451144, 1.393022248, 1.299617001, 1.125356691, 1.101406281, 1.30573597, 1.130580078, 0.901275863, 0.918949735, 0.976766828, 0.80359333, 0.931260063, 0.876791154, 1.109079044, 1.14320266, 1.029417219, 1.060623878, 1.256976224, 1.254247218, 1.101007781, 1.000741719, 1.141504549, 1.178572161, 0.988488212, 0.940178226, 0.798522697, 0.932244598, 1.097467105, 0.932775546, 0.878297562, 1.087764123, 1.166611838, 1.336440866, 1.356023657, 1.438686331, 1.485635552, 1.480443043, 1.54709473, 1.358955244, 1.330563044, 1.418889375, 1.231578492, 1.070392081, 1.103350922, 1.055773216, 1.17123807, 1.005658015, 1.12172986, 1.243541348, 1.179856545, 1.003558333, 1.109811078, 1.106150224, 0.844127533, 0.84315134, 0.957780165, 0.88548805, 1.090039833, 1.209517915, 1.198581146, 1.254055539, 1.020950473, 1.06415246, 1.173744361, 1.250414657, 1.144412688, 1.127179254, 1.123625057, 1.03958692, 1.037522863, 0.940047236, 0.983607069, 0.776961975, 0.647925635, 0.783498519, 0.736635082, 0.970655625, 1.072049264, 1.224623936, 1.252766614, 1.352190505, 1.363015392, 1.431606189, 1.425241251, 1.404458293, 1.425452837, 1.362857577, 1.219258532, 1.264323452, 1.270157868, 1.234217656, 1.197609084, 1.209324772, 1.004954359, 0.879971686, 0.867967986, 0.712899924, 0.792926381, 1.002084184, 1.086491597, 1.206458598, 0.94872125, 0.953289, 1.082618608, 0.860126494, 0.828870831, 0.800997293, 0.776295561, 0.937007071, 1.101182413, 0.928818564, 0.92786823, 1.103539804, 1.090989119, 0.934205055, 0.994661835, 1.145727913, 1.024830237, 0.896724066, 1.011635999, 1.089200062, 0.873984672, 0.809187072, 0.954179001, 0.820187244, 1.034372575, 1.047925989, 1.226495854, 1.304991266, 1.407771441, 1.447205567, 1.542829961, 1.568195979, 1.612361028, 1.474560238, 1.47125642, 1.366189421, 1.309559032, 1.356213393, 1.259783103, 1.27200196, 1.103740323, 1.143806408, 1.26544444, 1.265032351, 1.250454141, 1.042469749, 1.115198044, 1.287860012, 1.152502719, 0.95402407, 1.035110958, 1.199807386, 1.180360681, 0.980520306, 1.076055442, 1.209967661, 1.038163847, 0.892933522, 0.988078367, 1.048611927, 1.26397404, 1.279743112, 1.412078416, 1.474597646, 1.562757297, 1.644522449, 1.679863604, 1.478224472, 1.401511169, 1.439330011, 1.468539744, 1.455558713, 1.410084806, 1.353100374, 1.305076962, 1.190593744, 1.048639709, 0.817787197, 0.871946424, 0.983575124, 1.213443839, 1.335364741, 1.437150894, 1.495487573, 1.576474641, 1.633136131, 1.685742293, 1.582275604, 1.559283866, 1.406329166, 1.24129364, 1.254492198, 1.121941981, 1.013139554, 0.992852065, 1.016073515, 0.913108923, 1.061753527, 1.008918185, 0.792518122, 0.895728238, 1.017873096, 0.850132808, 0.755427564, 0.796661303, 1.058694598, 1.086760856, 1.010480181, 1.099840613, 1.151076291, 1.121074979, 1.208660875, 0.98269936, 0.937275363, 0.796115036, 1.006323396, 1.125034573, 1.377145213, 1.474385649, 1.516401571, 1.483379732, 1.374429914, 1.354322888, 1.225724061, 1.221243478, 1.045434285, 0.880129081, 0.824520226, 1.054468819, 1.226194165, 1.198247459, 1.300989566, 1.264360331, 1.341876601, 1.306651229, 1.271142458, 1.268679181, 0.95530231, 0.963132516, 0.909610761, 1.023792002, 0.993118272, 1.02255729, 1.052736126, 1.027354335, 1.065457054, 1.086478102, 0.953852182, 0.993332939, 0.965785522, 0.681324072], 
            '1pek':  [0.863125999, 0.970172358, 1.020781143, 0.882066695, 0.88077938, 1.142255548, 1.195687053, 1.225601426, 1.450308386, 1.4495013, 1.37301683, 1.368752988, 1.449070406, 1.291944789, 1.128256251, 0.962721576, 0.912207381, 1.004621603, 0.863599569, 0.933360004, 1.003546051, 1.086640502, 1.279994469, 1.135425894, 1.173959147, 1.042580758, 0.946619205, 1.016188436, 1.312257269, 1.483140595, 1.220372292, 1.140839714, 1.431912424, 1.463130986, 1.612154665, 1.580762757, 1.650405231, 1.586398353, 1.577223913, 1.49995823, 1.506628926, 1.466044454, 1.234708558, 1.197683868, 0.953281222, 1.093924413, 0.936742455, 1.1505593, 1.276450993, 0.988639911, 0.953017811, 1.149740698, 1.311866248, 1.176461919, 1.21146645, 1.084720646, 1.093265954, 1.149703371, 1.002413822, 0.902674748, 0.707322666, 0.838221665, 1.042183075, 1.056037965, 1.279995313, 1.023033591, 1.157724583, 1.314131963, 1.412204975, 1.602355233, 1.560055177, 1.559798125, 1.672814746, 1.658782552, 1.642032957, 1.690092559, 1.758538468, 1.648654358, 1.492101473, 1.211474482, 1.145615288, 1.398026939, 1.630585851, 1.57193841, 1.579347451, 1.378387485, 1.270197733, 1.461455885, 1.33960146, 1.486100378, 1.427858831, 1.51139607, 1.46249425, 1.453982575, 1.361523312, 1.371703362, 1.134537194, 1.072897721, 0.953018358, 1.203799174, 1.11176269, 1.080556235, 0.975754129, 1.068991161, 0.951779524, 1.09953035, 1.309933384, 1.2196839, 1.10115923, 1.300338994, 1.352300356, 1.129604548, 1.129205865, 1.287755566, 1.181897843, 0.961503934, 1.033096981, 1.11693809, 0.871326824, 0.79294515, 0.924544158, 0.870860852, 1.12743026, 0.941423006, 1.158834823, 1.28810718, 1.437195382, 1.621336854, 1.634683902, 1.720235726, 1.660715055, 1.703831021, 1.585574664, 1.436446322, 1.233280138, 1.03941807, 1.04367786, 1.001149426, 0.910787725, 0.956058542, 1.231630605, 1.281942928, 1.096923741, 1.218071477, 1.386530398, 1.218221638, 1.096472381, 1.323771306, 1.341634867, 1.042234454, 1.022239279, 1.117245332, 1.400453426, 1.53096813, 1.577048319, 1.690021744, 1.701255652, 1.729005676, 1.609723453, 1.483122968, 1.313227844, 1.052681431, 1.081169809, 1.029578962, 1.084768716, 1.318809062, 1.086644424, 1.019375646, 1.302678817, 1.415290558, 1.478852403, 1.522139648, 1.304974257, 1.257333798, 1.097895478, 1.105847499, 1.399688742, 1.520065806, 1.603849331, 1.695308326, 1.616820885, 1.630689228, 1.48340722, 1.269403214, 1.089621957, 0.948479798, 1.139302431, 1.127705554, 1.254344221, 1.292767013, 1.001829829, 1.161818757, 1.413904584, 1.402038782, 1.279981505, 1.151452769, 1.030852403, 1.172702557, 1.39400529, 1.359090582, 1.490374196, 1.584950958, 1.642081627, 1.579358101, 1.628710598, 1.33040298, 1.201793879, 1.379710561, 1.265971181, 1.410674031, 1.37174248, 1.264780505, 1.106082809, 0.84417518, 0.933686631, 0.934514781, 1.084973118, 1.043902639, 1.15688763, 1.212461412, 1.338759989, 1.514103894, 1.699402093, 1.722054841, 1.673030718, 1.779106069, 1.795718844, 1.793794618, 1.722476798, 1.700049381, 1.744415162, 1.746384113, 1.604902204, 1.582381137, 1.60167286, 1.513927848, 1.361719808, 1.363477896, 1.263543797, 1.081263973, 0.973588808, 0.989670813, 1.117884428, 1.156020263, 1.337106823, 1.1161077, 1.109649584, 1.370752533, 1.382793209, 1.140154098, 1.171473787, 1.362701044, 1.261655194, 1.004348083, 1.078475218, 1.277816527, 1.140226344, 1.012917721, 0.898015584, 0.981421198, 1.140033874, 0.957750553, 0.904171066, 1.01692806, 0.869986318, 0.733865672, 0.82153369, 1.103528677, 1.102301577, 1.135304255, 1.302895365, 1.426163313, 1.493709284, 1.382563367, 1.291125368, 1.05431133, 1.026157468, 0.772423008, 0.646091901], 
            '2ppn':  [0.657953869, 0.841356297, 0.726683406, 0.798976252, 0.693844335, 0.734069713, 0.669324701, 0.645716197, 0.656420573, 0.810343216, 0.603968043, 0.590700783, 0.537115989, 0.637596624, 0.745416729, 0.765731796, 0.62027794, 0.623329542, 0.617866817, 0.707081614, 0.792005642, 0.89924516, 0.868129448, 0.944620891, 0.88319047, 0.938511957, 0.891671755, 0.919358187, 0.888302507, 0.805412593, 0.673828015, 0.542023207, 0.613295671, 0.610994874, 0.724414237, 0.681001618, 0.714137928, 0.805231112, 0.798858526, 0.704100178, 0.57818406, 0.563722547, 0.552125992, 0.584581956, 0.723276582, 0.757119762, 0.752883109, 0.773218906, 0.778259174, 0.833709522, 0.67451591, 0.614147688, 0.655272234, 0.629413664, 0.757823113, 0.821481826, 0.824979112, 0.960458145, 0.967814607, 0.900583157, 0.823517256, 0.944904865, 0.965712097, 0.852490079, 0.768507473, 0.885473383, 0.882310227, 0.83570154, 0.78946783, 0.934101268, 0.90924107, 0.940544246, 0.895161325, 0.973638286, 0.877672527, 0.952896146, 0.825773446, 0.867279114, 0.694613074, 0.844740513, 0.880637387, 0.775921583, 0.739715389, 0.59492948, 0.577725698, 0.768092639, 0.630862746, 0.535137974, 0.471093829, 0.593353583, 0.737237703, 0.660106416, 0.66935054, 0.683946648, 0.772478281, 0.812277133, 0.916965302, 0.921796166, 0.983790323, 0.914488741, 0.990412163, 0.950121082, 0.965720801, 0.791137922, 0.724681793, 0.725162947, 0.543210273]}

def calculate_dnds_h(generating_model, protein):
    '''
        Extracts expeced site-specific rates
    '''
    if generating_model == "Ne2_C-SI" or generating_model == "Ne2_S-SI":        
        Kn = np.genfromtxt(RstPath + 'dNdS/' +  protein + "_" + 
                           generating_model +'_Kn.csv', delimiter=' ')
        Ln = np.genfromtxt(RstPath + 'dNdS/' + protein + "_" + 
                           generating_model +'_Ln.csv', delimiter=' ')
        return(Kn, Ln)
    elif generating_model == "Ne2_S-SD":
        Kn = []; Ln = []
        for trial in range(1,51):
            full_Kn = np.genfromtxt(RstPath +'dNdS/' +  protein + "_" + 
                                    generating_model + '_Kn_Ln/Kn_' + 
                                    str(trial) + '.csv', delimiter=' ')
            full_Ln = np.genfromtxt(RstPath +'dNdS/' +  protein + "_" + 
                                    generating_model + '_Kn_Ln/Ln_' + 
                                    str(trial) + '.csv', delimiter=' ')
            Kn.append(np.sum(full_Kn, axis = 0))
            Ln.append(np.sum(full_Ln, axis = 0))
        return(np.array(Kn), np.array(Ln))
        

def rate_RSA_correlation(dnds_h, protein, dictionary):
    #RSA# 
    RSA = dictionary[protein]
    R = []; P = []
    for trial in range(50):
        omega = dnds_h[trial]
        r, p = stats.pearsonr(omega, RSA)
        R.append(r)
        P.append(p)
    return(np.array(R), np.array(P))


#%% Report correlations per model per protein-specific simulation
rst_wcn = {}
rst_rsa = {}
for protein in ['1qhw', '2ppn', '1pek']:
    print('\n', protein, '\n')
    for model in ['Ne2_C-SI', 'Ne2_S-SI', 'Ne2_S-SD']:
        
        #dN^h/dS^h#
        full_Kn, full_Ln = calculate_dnds_h(model, protein)
        dnds_h = full_Kn / full_Ln
    	
        
        #correlation#
        R, P = rate_RSA_correlation(dnds_h, protein, rsa_dict)
        sig = [P <= 0.005]
        print ('RSA:\n ' + str(model) + " \n mean R (std) Pvalue " + 
               "%.3f" % np.mean(R) + "(" + "%.3f" % np.std(R) + ") " + 
               "%.3f" % np.mean(P) + " \n Number of significant trials " +
               str(np.sum(sig)))
        rst_rsa[protein + "_" + model] = (np.mean(R), np.std(R))


        #correlation#
        R, P = rate_RSA_correlation(dnds_h, protein, wcn_dict)
        sig = [P <= 0.005]
        print ('WCN:\n ' + str(model) + " \n mean R (std) Pvalue " + 
               "%.3f" % np.mean(R) + "(" + "%.3f" % np.std(R) + ") " + 
               "%.3f" % np.mean(P) + " \n Number of significant trials " +
               str(np.sum(sig)))
        rst_wcn[protein + "_" + model] = (np.mean(R), np.std(R))


#%% Plotting 
fig, (ax1, ax2)  = plt.subplots(2, 1, sharex = True, figsize = (5, 7))

m = ['o', 'd', 's']
l = ['1QHW', '2PPN', '1PEK']

#RSA# 
for i, (x, y) in enumerate(zip([0,0.1, 0.2],([rst_rsa['1qhw_Ne2_C-SI'], rst_rsa['2ppn_Ne2_C-SI'], rst_rsa['1pek_Ne2_C-SI']]))):
    ax1.errorbar(x, y[0], yerr =y[1], color = 'darkblue', marker = m[i])

for i, (x, y) in enumerate(zip([0.5,0.6, 0.7],([rst_rsa['1qhw_Ne2_S-SI'], rst_rsa['2ppn_Ne2_S-SI'], rst_rsa['1pek_Ne2_S-SI']]))):
    ax1.errorbar(x, y[0], yerr =y[1], color = 'darkred', marker = m[i])

for i, (x, y) in enumerate(zip([1,1.1, 1.2],([rst_rsa['1qhw_Ne2_S-SD'], rst_rsa['2ppn_Ne2_S-SD'], rst_rsa['1pek_Ne2_S-SD']]))):
    ax1.errorbar(x, y[0], yerr =y[1], color = 'chocolate', marker = m[i])

for i, (x, y) in enumerate(zip([1,1.1, 1.2],([rst_rsa['1qhw_Ne2_S-SD'], rst_rsa['2ppn_Ne2_S-SD'], rst_rsa['1pek_Ne2_S-SD']]))):
##for i, (x, y) in enumerate(zip([2.1,2.2, 2.3],([r_qhw_M3k3, r_ppn_M3k2, r_pek_M3k3]))):
    ax1.scatter(x, y[0], color = 'k', marker = m[i], label= l[i])

ax1.axhline(0, color = 'k', linewidth = 2, linestyle = ":")

ax1.set_ylim(-0.15, 0.55)
ax1.set_ylabel('correlation coefficient between \n RSA and $dN^h/dS^h$', fontsize = 10)
ax1.legend(loc='upper left')

#WCN
for i, (x, y) in enumerate(zip([0,0.1, 0.2],([rst_wcn['1qhw_Ne2_C-SI'], rst_wcn['2ppn_Ne2_C-SI'], rst_wcn['1pek_Ne2_C-SI']]))):
    ax2.errorbar(x, y[0], yerr =y[1], color = 'darkblue', marker = m[i])

for i, (x, y) in enumerate(zip([0.5,0.6, 0.7],([rst_wcn['1qhw_Ne2_S-SI'], rst_wcn['2ppn_Ne2_S-SI'], rst_wcn['1pek_Ne2_S-SI']]))):
    ax2.errorbar(x, y[0], yerr =y[1], color = 'darkred', marker = m[i])

for i, (x, y) in enumerate(zip([1,1.1, 1.2],([rst_wcn['1qhw_Ne2_S-SD'], rst_wcn['2ppn_Ne2_S-SD'], rst_wcn['1pek_Ne2_S-SD']]))):
    ax2.errorbar(x, y[0], yerr =y[1], color = 'chocolate', marker = m[i])

for i, (x, y) in enumerate(zip([1,1.1, 1.2],([rst_wcn['1qhw_Ne2_S-SD'], rst_wcn['2ppn_Ne2_S-SD'], rst_wcn['1pek_Ne2_S-SD']]))):
##for i, (x, y) in enumerate(zip([2.1,2.2, 2.3],([r_qhw_M3k3, r_ppn_M3k2, r_pek_M3k3]))):
    ax2.scatter(x, y[0], color = 'k', marker = m[i], label= l[i])

ax2.axhline(0, color = 'k', linewidth = 2, linestyle = ":")

ax2.set_ylim(-0.55, 0.15)
ax2.set_ylabel('correlation coefficient between \n WCN and $dN^h/dS^h$', fontsize = 10)
plt.xticks([0.1, 0.6, 1.1], ['C-SI', 'S-SI', 'S-SD'], fontsize = 12)

[t.set_color(i) for (i,t) in zip(["darkblue", "darkred", "chocolate"],ax2.xaxis.get_ticklabels())]


plt.savefig('../Figures/Figure3.png', dpi = 450, bbox_inches = 'tight')


