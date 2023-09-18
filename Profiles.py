






def load_profile(person):
    Glyn_list = ["Glyn", "Glyn_15cM", "Glyn_14cM","Glyn_13cM", "Glyn_12cM", "Glyn_11cM", "Glyn_10cM",
                 "Glyn_9cM", "Glyn_8cM", "Glyn_7cM", "Glyn_6cM", "Glyn_B"]
    Wayne_list = ["Wayne","Wayne_15cM", "Wayne_14cM","Wayne_13cM", "Wayne_12cM", "Wayne_11cM","Wayne_10cM",
                  "Wayne_9cM", "Wayne_8cM", "Wayne_7cM", "Wayne_6cM"]
    Helen_list = ["Helen", "Helen_B", "Helen_L"]
    Elwyn_list = ["Elwyn", "Elwyn_15cM", "Elwyn_14cM", "Elwyn_13cM", "Elwyn_12cM", "Elwyn_11cM",
                  "Elwyn_10cM", "Elwyn_9cM"]
    Anji_list = ["Anji", "Anji_15cM", "Anji_14cM", "Anji_13cM", "Anji_12cM", "Anji_11cM", "Anji_10cM",
                 "Anji_9cM", "Anji_8cM"]
    Marg_list = ["Marg", "Marg_15cM", "Marg_14cM", "Marg_13cM", "Marg_12cM", "Marg_11cM"]
    Sally_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM", "Sally_L"]
    Una_list = ["Una", "Una_15cM", "Una_14cM", "Una_13cM", "Una_12cM", "Una_11cM", "Una_10cM", "Una_9cM", "Una_8cM",
                "Una_7cM", "Una_6cM", "Una_L"]
    Gary_list = ["Gary", "Gary_15cM", "Gary_14cM", "Gary_13cM", "Gary_12cM", "Gary_11cM", "Gary_10cM",
                      "Gary_9cM", "Gary_8cM"]

    if person == "Glyn":
        match_filter_list = ["aberlas", "UJonesManagedbySteamerpoint", "SallyAnneGale", "H.H.ManagedbyReesDinbych",
                             "gethngethn",
                             "FrancesSandraKey",
                             "TecwynRawson",  # collides with Buckle
                             "ArthurMarkGaleManagedbySteamerpoint", "BarbaraParryManagedbyGwendaParfitt",
                             "D.W.ManagedbyWendyMcKenna",
                             "ElizabethPritchard", "sheree8", "AlwenaJames", "LJ", "thesmiths122",
                             "LindaJones","WilliamCarney"]
        match_filter_list2 = [
          #  "EricEngelhard",
            "NatalieRoberts_53%",
            "StevenRoberts_100%",
            "nora_engelhard",
            "JudithBuckle",
        #    "patsobocienski",
            "SimonGray"]
        match_filter_list3 = [
      #                        "G.R.Managedbygemmaroberts50",
                              "H.D.Managedbyprenjo", "usersam2772",
                              "DellaPritchard",
                           #   "IforGlynLloyd",
                           #      E.G.ManagedbyKarenBracegirdle",
                           #      "JudyJones",
                              "HenryRobertsManagedbyHollyMonday-Jones"]
        match_filter_list4 = ["ElizabethPritchard",
                              "AdelynEllis", "CliffordDaviesManagedbychezdavies92",
                              "DewiPugh", "ElwynDavies", "GlynParry",
                              "gwendahumphries", "InaBlancheParry"]

        match_filter_list5 = ["JaredDeWittie"]

        match_filter_list6 = ["PaulDay", "LKevinKelly11", "tchester200166", "ADavis0214", "JohnKelly",
#                              "ErinWilson", "ColleenOLeary", "AnnStoddard", "RebeccaBailey", "arwelwjones51",
                              "ErinWilson", "ColleenOLeary", "AnnStoddard", "arwelwjones51",
                              "JuneMcLachlinManagedbyoschean"]
        match_filter_list7 = ["GillianandGlynEvans", "D.H.ManagedbySEANALLEN"]
        match_filter_list8 = ["stevemcgarry189", "BrianLonghurst",
                              "MalcolmSlade", "ClaireDayel-Baker", "judyrobinson"]
        match_filter_list9 = ["ElenLewis"]
#        match_filter_list10 = ["AmandaStanton", "JohnNolan573ManagedbySianShrewsbury", "RayRutland65"]
        match_filter_bobcollins = ["InaBlancheParry","SionElganMetcalfe","GarethWilliams","LeonaCarter"]
        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)
        match_filter_list.extend(match_filter_list6)
        match_filter_list.extend(match_filter_list7)
        match_filter_list.extend(match_filter_list8)
        match_filter_list.extend(match_filter_list9)
#        match_filter_list.extend(match_filter_list10)
        match_filter_list.extend(match_filter_bobcollins)
        kit1_file_list = Glyn_list
        kit2_file_list = Wayne_list
        kit3_file_list = Gary_list
        kit4_file_list = Elwyn_list
        kit5_file_list = Sally_list
        kit6_file_list = Helen_list

    if person == "Wayne":
        kit1_file_list = Wayne_list
        kit2_file_list = Glyn_list
        kit3_file_list = Gary_list
        kit4_file_list = Elwyn_list
        kit5_file_list = Una_list
        kit6_file_list = Sally_list
        match_filter_list = [ "ag3754", "DavidLarsen", "sheilaroberts",
                         "BarbaraParryManagedbyGwendaParfitt", "aberlas","UJonesManagedbySteamerpoint","H.H.ManagedbyReesDinbych"]
#        match_filter_list2 = ["ThomasBennett","malcolmdavies656"]
        match_filter_list2 = ["ThomasBennett"]
        match_filter_list.extend(match_filter_list2)
        match_filter_list3 = ["PaulineWilliams", "LindaEvans", "susanwhiskin", "MichaelEvans"]
        match_filter_list.extend(match_filter_list3)
        match_filter_list4 = ["nogoodboyoManagedbyRhiannonWilliams", "craftyhen"]
        match_filter_list.extend(match_filter_list4)
        match_filter_list6 = ["GaryWilliams", "ElwynWilliams","SandraDavis","LauraStupple", "C.H.Managedbykeiralynch99"]
        match_filter_list.extend(match_filter_list6)


    if person == "Gary":
        match_filter_list = ["DavidLarsen","sheilarobertsManagedbySheilaRoberts","InaBlancheParry","opj142"]
        match_filter_list2 = ["nogoodboyoManagedbyRhiannonWilliams"]
        match_filter_list3 = ["aberlas", "AuntUnaManagedbySteamerpoint", "SallyAnneGale", "H.H.ManagedbyReesDinbych","gethngethn", \
                              "LaurenJames", "BarbaraParryManagedbyGwendaParfitt", "ArthurMarkGaleManagedbySteamerpoint"]
        match_filter_list4 = ["nogoodboyoManagedbyRhiannonWilliams", "craftyhen","ThomasBennett"]
        match_filter_list5 = ["MichaelEvans", "PaulineWilliams","LindaEvans","susanwhiskin"]
        match_filter_list6 = ["WayneWilliams", "ElwynWilliams","SandraDavis","LauraStupple"]
        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)
        match_filter_list.extend(match_filter_list6)

        kit1_file_list = Gary_list
        kit2_file_list = Wayne_list
        kit3_file_list = Elwyn_list
        kit4_file_list = Glyn_list
        kit5_file_list = Marg_list
        kit6_file_list = Helen_list

    if person == "Elwyn":
        kit1_file_list = Elwyn_list
        kit2_file_list = Wayne_list
        kit3_file_list = Gary_list
        kit4_file_list = Glyn_list
        kit5_file_list = Sally_list
        kit6_file_list = Helen_list

        match_filter_list = ["aberlas"]
        match_filter_list2 = ["LauraStupple", "GaryWilliams", "SandraDavis", "WayneWilliams","malcolmdavies656"]
        match_filter_list3 = ["PaulineWilliams", "susanwhiskin", "MichaelEvans", "LindaEvans", "DawnTudor"]
        match_filter_list4 = []
        match_filter_list5 = []
        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)


    if person == "Sally":
        match_filter_list = ["UJonesManagedbySteamerpoint", "RobertFort", "LaurenRoberts", "DavidRobertsManagedbyLaurenRoberts","WynneOwens"]
        match_filter_list2 = ["JenniferNydahl",  "gpb444", "reina155", "uklancsbabe","gethngethn"]
        match_filter_list.extend(match_filter_list2)
        match_filter_list3 = [ "lambbhuna","MyfanwyWilliams-Owen", "AnnaLouiseYoud", "WilliamBarhydt"] # "LeanneHodgeon"
        match_filter_list.extend(match_filter_list3)
        match_filter_list4 = ["GlynWilliams","WayneWilliams","aberlas"]
        match_filter_list.extend(match_filter_list4)
        match_filter_list5 = ["haulfre8", "anncj_bowman"]
        match_filter_list.extend(match_filter_list5)
        match_filter_list6 = ["M.W.Managedbyrodwilson", "N.C.ManagedbyGeoffCreighton", "EricNaylor"]
        match_filter_list.extend(match_filter_list6)

        kit1_file_list = Sally_list
        kit2_file_list = Una_list
        kit3_file_list = Glyn_list
        kit4_file_list = Wayne_list
        kit6_file_list = Helen_list
        kit5_file_list = Gary_list

    if person == "Una":
        kit1_file_list = Una_list
        kit2_file_list = Sally_list
        kit3_file_list = Glyn_list
        kit4_file_list = Wayne_list
        kit5_file_list = Helen_list
        kit6_file_list = Anji_list

        match_filter_list = ["SallyAnneGale","MaryCrawford","ArthurMarkGaleManagedbySteamerpoint","XantheCrawford","QuintinCrawford"]
        match_filter_list2 = ["GlynWilliams","gethngethn","ElenLewis","GaryWilliams","aberlas","TecwynRawson"]
        match_filter_list.extend(match_filter_list2)
        cluster_21 = ["DebbieParsons","NiaJones","PhilipDee","AnnStoddard","VioletWilliams","matt47811","PaulaStoddard-Jones"]
        match_filter_list.extend(cluster_21)
        cluster_57 = ["edwardagwyneth","MyfanwyWilliams-Owen","GailJones" ]
        match_filter_list.extend(cluster_57)
        cluster_Helen = ["D.W.ManagedbyWendyMcKenna","7glyndwr8","CarysDuggan-Rees","FionaEdwards" ]
        match_filter_list.extend(cluster_Helen)
        cluster_Anji = ["DellaPritchard", "InaBlancheParry", "donnawals3", "JaneDonnelly", "AlwenaLadell", "ffionjones"]
        match_filter_list.extend(cluster_Anji)

    if person == "Helen":
        kit1_file_list = Helen_list
        kit2_file_list = Glyn_list
        kit3_file_list = Wayne_list
        kit4_file_list = Gary_list
        kit5_file_list = Una_list
        kit6_file_list = Sally_list

        match_filter_list = ["aberlas","JohnRoberts","JulieAllam", "ArwelHughes"]
        match_filter_list2 = ["GlynWilliams","WayneWilliams","GaryWilliams"]
        match_filter_list3 = ["MeinirMaiJones"]
        match_filter_list4 = ["JohnPrice","DanielHowell","MaldwynJones" ,"KevinMcFall"]
        match_filter_list5 = ["WillAtkinson","RichardParker","RhiannonJonesManagedbyKelvinJones"]
        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)

    if person == "Anji":
        kit1_file_list = Anji_list
        kit2_file_list = Glyn_list
        kit3_file_list = Una_list
        kit4_file_list = Sally_list
        kit5_file_list = Gary_list
        kit6_file_list = Wayne_list

        match_filter_list = ["MabelBiddulph", "jebrammar", "DannyDunk", "nicholasBrookfield", "KarenBowring"]
     #   match_filter_list = []
        match_filter_list2 = ["S.E.Managedbygmentwistle1"]
        match_filter_list3 = []
        match_filter_list4 = []
        match_filter_list5 = []
        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)

    if person == "Marg":
        kit1_file_list = Marg_list
        kit2_file_list = Wayne_list
        kit3_file_list = Gary_list
        kit4_file_list = Elwyn_list
        kit5_file_list = Glyn_list
        kit6_file_list = Una_list
        match_filter_list2 = []
        match_filter_list = ["MabelBiddulph"]
        match_filter_list3 = []
        match_filter_list4 = []
        match_filter_list5 = []
        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)


    return kit1_file_list, kit2_file_list, kit3_file_list, kit4_file_list, kit5_file_list, kit6_file_list, match_filter_list
