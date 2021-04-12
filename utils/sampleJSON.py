import uuid

"""
'array_of_docs' : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    },
    {
    	   "sclr" : 12,
        "str" : "g",
        "arr" : [7,8,9,{"sclr" : 22, "str" : "h"}]
        },
    -2
    ]
"""

smallObj= {
'sclr' : 0,
'str' : "b",
'sub_doc' : {
	"sclr" : 10,
	"str" : "c",
	"arr" : [1,2,3,{"sclr" : 20, "str":"d"}]
},
'array_of_docs' : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }]
}


"""
"object with 1 member":["array with 1 element"]}, 3.39 KB
    {},
    [],
    -42,
    True,
    False,
    null,
"""
bigObj={
"type": "bigObj",
"web-app": {
  "servlet": [   
    {
      "servlet-name": "cofaxCDS",
      "servlet-class": "org.cofax.cds.CDSServlet",
      "init-param": {
        "configGlossary:installationAt": "Philadelphia, PA",
        "configGlossary:adminEmail": "ksm@pobox.com",
        "configGlossary:poweredBy": "Cofax",
        "configGlossary:poweredByIcon": "/images/cofax.gif",
        "configGlossary:staticPath": "/content/static",
        "templateProcessorClass": "org.cofax.WysiwygTemplate",
        "templateLoaderClass": "org.cofax.FilesTemplateLoader",
        "templatePath": "templates",
        "templateOverridePath": "",
        "defaultListTemplate": "listTemplate.htm",
        "defaultFileTemplate": "articleTemplate.htm",
        "useJSP": False,
        "jspListTemplate": "listTemplate.jsp",
        "jspFileTemplate": "articleTemplate.jsp",
        "cachePackageTagsTrack": 200,
        "cachePackageTagsStore": 200,
        "cachePackageTagsRefresh": 60,
        "cacheTemplatesTrack": 100,
        "cacheTemplatesStore": 50,
        "cacheTemplatesRefresh": 15,
        "cachePagesTrack": 200,
        "cachePagesStore": 100,
        "cachePagesRefresh": 10,
        "cachePagesDirtyRead": 10,
        "searchEngineListTemplate": "forSearchEnginesList.htm",
        "searchEngineFileTemplate": "forSearchEngines.htm",
        "searchEngineRobotsDb": "WEB-INF/robots.db",
        "useDataStore": True,
        "dataStoreClass": "org.cofax.SqlDataStore",
        "redirectionClass": "org.cofax.SqlRedirection",
        "dataStoreName": "cofax",
        "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
        "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
        "dataStoreUser": "sa",
        "dataStorePassword": "dataStoreTestQuery",
        "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
        "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
        "dataStoreInitConns": 10,
        "dataStoreMaxConns": 100,
        "dataStoreConnUsageLimit": 100,
        "dataStoreLogLevel": "debug",
        "maxUrlLength": 500}},
    {
      "servlet-name": "cofaxEmail",
      "servlet-class": "org.cofax.cds.EmailServlet",
      "init-param": {
      "mailHost": "mail1",
      "mailHostOverride": "mail2"}},
    {
      "servlet-name": "cofaxAdmin",
      "servlet-class": "org.cofax.cds.AdminServlet"},
 
    {
      "servlet-name": "fileServlet",
      "servlet-class": "org.cofax.cds.FileServlet"},
    {
      "servlet-name": "cofaxTools",
      "servlet-class": "org.cofax.cms.CofaxToolsServlet",
      "init-param": {
        "templatePath": "toolstemplates/",
        "log": 1,
        "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
        "logMaxSize": "",
        "dataLog": 1,
        "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
        "dataLogMaxSize": "",
        "removePageCache": "/content/admin/remove?cache=pages&id=",
        "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
        "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
        "lookInContext": 1,
        "adminGroupID": 4,
        "betaServer": True}}],
  "servlet-mapping": {
    "cofaxCDS": "/",
    "cofaxEmail": "/cofaxutil/aemail/*",
    "cofaxAdmin": "/admin/*",
    "fileServlet": "/static/*",
    "cofaxTools": "/tools/*"},
 
  "taglib": {
    "taglib-uri": "cofax.tld",
    "taglib-location": "/WEB-INF/tlds/cofax.tld"}}
}





"""
"Pokemon gaming sample object 
"""



hugeObj={
    "damage_relations": {
        "double_damage_from": [
            {
                "name": "fighting",
                "url": "https://pokeapi.co/api/v2/type/2/"
            }
        ],
        "double_damage_to": [],
        "half_damage_from": [],
        "half_damage_to": [
            {
                "name": "rock",
                "url": "https://pokeapi.co/api/v2/type/6/"
            },
            {
                "name": "steel",
                "url": "https://pokeapi.co/api/v2/type/9/"
            }
        ],
        "no_damage_from": [
            {
                "name": "ghost",
                "url": "https://pokeapi.co/api/v2/type/8/"
            }
        ],
        "no_damage_to": [
            {
                "name": "ghost",
                "url": "https://pokeapi.co/api/v2/type/8/"
            }
        ]
    },
    "generation": {
        "name": "generation-i",
        "url": "https://pokeapi.co/api/v2/generation/1/"
    },
    "move_damage_class": {
        "name": "physical",
        "url": "https://pokeapi.co/api/v2/move-damage-class/2/"
    },
    "name": "normal",
    "names": [
        {
            "language": {
                "name": "ja-Hrkt",
                "url": "https://pokeapi.co/api/v2/language/1/"
            },
            "name": "ノーマル"
        },
        {
            "language": {
                "name": "ko",
                "url": "https://pokeapi.co/api/v2/language/3/"
            },
            "name": "노말"
        },
        {
            "language": {
                "name": "fr",
                "url": "https://pokeapi.co/api/v2/language/5/"
            },
            "name": "Normal"
        },
        {
            "language": {
                "name": "de",
                "url": "https://pokeapi.co/api/v2/language/6/"
            },
            "name": "Normal"
        },
        {
            "language": {
                "name": "es",
                "url": "https://pokeapi.co/api/v2/language/7/"
            },
            "name": "Normal"
        },
        {
            "language": {
                "name": "it",
                "url": "https://pokeapi.co/api/v2/language/8/"
            },
            "name": "Normale"
        },
        {
            "language": {
                "name": "en",
                "url": "https://pokeapi.co/api/v2/language/9/"
            },
            "name": "Normal"
        }
    ],
    "pokemon": [
        {
            "pokemon": {
                "name": "pidgey",
                "url": "https://pokeapi.co/api/v2/pokemon/16/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "pidgeotto",
                "url": "https://pokeapi.co/api/v2/pokemon/17/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "pidgeot",
                "url": "https://pokeapi.co/api/v2/pokemon/18/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "rattata",
                "url": "https://pokeapi.co/api/v2/pokemon/19/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "raticate",
                "url": "https://pokeapi.co/api/v2/pokemon/20/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "spearow",
                "url": "https://pokeapi.co/api/v2/pokemon/21/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "fearow",
                "url": "https://pokeapi.co/api/v2/pokemon/22/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "jigglypuff",
                "url": "https://pokeapi.co/api/v2/pokemon/39/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "wigglytuff",
                "url": "https://pokeapi.co/api/v2/pokemon/40/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "meowth",
                "url": "https://pokeapi.co/api/v2/pokemon/52/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "persian",
                "url": "https://pokeapi.co/api/v2/pokemon/53/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "farfetchd",
                "url": "https://pokeapi.co/api/v2/pokemon/83/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "doduo",
                "url": "https://pokeapi.co/api/v2/pokemon/84/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "dodrio",
                "url": "https://pokeapi.co/api/v2/pokemon/85/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "lickitung",
                "url": "https://pokeapi.co/api/v2/pokemon/108/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "chansey",
                "url": "https://pokeapi.co/api/v2/pokemon/113/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "kangaskhan",
                "url": "https://pokeapi.co/api/v2/pokemon/115/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "tauros",
                "url": "https://pokeapi.co/api/v2/pokemon/128/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "ditto",
                "url": "https://pokeapi.co/api/v2/pokemon/132/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "eevee",
                "url": "https://pokeapi.co/api/v2/pokemon/133/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "porygon",
                "url": "https://pokeapi.co/api/v2/pokemon/137/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "snorlax",
                "url": "https://pokeapi.co/api/v2/pokemon/143/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "sentret",
                "url": "https://pokeapi.co/api/v2/pokemon/161/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "furret",
                "url": "https://pokeapi.co/api/v2/pokemon/162/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "hoothoot",
                "url": "https://pokeapi.co/api/v2/pokemon/163/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "noctowl",
                "url": "https://pokeapi.co/api/v2/pokemon/164/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "igglybuff",
                "url": "https://pokeapi.co/api/v2/pokemon/174/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "aipom",
                "url": "https://pokeapi.co/api/v2/pokemon/190/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "girafarig",
                "url": "https://pokeapi.co/api/v2/pokemon/203/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "dunsparce",
                "url": "https://pokeapi.co/api/v2/pokemon/206/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "teddiursa",
                "url": "https://pokeapi.co/api/v2/pokemon/216/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "ursaring",
                "url": "https://pokeapi.co/api/v2/pokemon/217/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "porygon2",
                "url": "https://pokeapi.co/api/v2/pokemon/233/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "stantler",
                "url": "https://pokeapi.co/api/v2/pokemon/234/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "smeargle",
                "url": "https://pokeapi.co/api/v2/pokemon/235/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "miltank",
                "url": "https://pokeapi.co/api/v2/pokemon/241/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "blissey",
                "url": "https://pokeapi.co/api/v2/pokemon/242/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "zigzagoon",
                "url": "https://pokeapi.co/api/v2/pokemon/263/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "linoone",
                "url": "https://pokeapi.co/api/v2/pokemon/264/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "taillow",
                "url": "https://pokeapi.co/api/v2/pokemon/276/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "swellow",
                "url": "https://pokeapi.co/api/v2/pokemon/277/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "slakoth",
                "url": "https://pokeapi.co/api/v2/pokemon/287/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "vigoroth",
                "url": "https://pokeapi.co/api/v2/pokemon/288/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "slaking",
                "url": "https://pokeapi.co/api/v2/pokemon/289/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "whismur",
                "url": "https://pokeapi.co/api/v2/pokemon/293/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "loudred",
                "url": "https://pokeapi.co/api/v2/pokemon/294/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "exploud",
                "url": "https://pokeapi.co/api/v2/pokemon/295/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "azurill",
                "url": "https://pokeapi.co/api/v2/pokemon/298/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "skitty",
                "url": "https://pokeapi.co/api/v2/pokemon/300/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "delcatty",
                "url": "https://pokeapi.co/api/v2/pokemon/301/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "spinda",
                "url": "https://pokeapi.co/api/v2/pokemon/327/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "swablu",
                "url": "https://pokeapi.co/api/v2/pokemon/333/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "zangoose",
                "url": "https://pokeapi.co/api/v2/pokemon/335/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "castform",
                "url": "https://pokeapi.co/api/v2/pokemon/351/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "kecleon",
                "url": "https://pokeapi.co/api/v2/pokemon/352/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "starly",
                "url": "https://pokeapi.co/api/v2/pokemon/396/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "staravia",
                "url": "https://pokeapi.co/api/v2/pokemon/397/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "staraptor",
                "url": "https://pokeapi.co/api/v2/pokemon/398/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "bidoof",
                "url": "https://pokeapi.co/api/v2/pokemon/399/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "bibarel",
                "url": "https://pokeapi.co/api/v2/pokemon/400/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "ambipom",
                "url": "https://pokeapi.co/api/v2/pokemon/424/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "buneary",
                "url": "https://pokeapi.co/api/v2/pokemon/427/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "lopunny",
                "url": "https://pokeapi.co/api/v2/pokemon/428/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "glameow",
                "url": "https://pokeapi.co/api/v2/pokemon/431/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "purugly",
                "url": "https://pokeapi.co/api/v2/pokemon/432/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "happiny",
                "url": "https://pokeapi.co/api/v2/pokemon/440/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "chatot",
                "url": "https://pokeapi.co/api/v2/pokemon/441/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "munchlax",
                "url": "https://pokeapi.co/api/v2/pokemon/446/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "lickilicky",
                "url": "https://pokeapi.co/api/v2/pokemon/463/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "porygon-z",
                "url": "https://pokeapi.co/api/v2/pokemon/474/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "regigigas",
                "url": "https://pokeapi.co/api/v2/pokemon/486/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "arceus",
                "url": "https://pokeapi.co/api/v2/pokemon/493/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "patrat",
                "url": "https://pokeapi.co/api/v2/pokemon/504/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "watchog",
                "url": "https://pokeapi.co/api/v2/pokemon/505/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "lillipup",
                "url": "https://pokeapi.co/api/v2/pokemon/506/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "herdier",
                "url": "https://pokeapi.co/api/v2/pokemon/507/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "stoutland",
                "url": "https://pokeapi.co/api/v2/pokemon/508/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "pidove",
                "url": "https://pokeapi.co/api/v2/pokemon/519/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "tranquill",
                "url": "https://pokeapi.co/api/v2/pokemon/520/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "unfezant",
                "url": "https://pokeapi.co/api/v2/pokemon/521/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "audino",
                "url": "https://pokeapi.co/api/v2/pokemon/531/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "minccino",
                "url": "https://pokeapi.co/api/v2/pokemon/572/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "cinccino",
                "url": "https://pokeapi.co/api/v2/pokemon/573/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "deerling",
                "url": "https://pokeapi.co/api/v2/pokemon/585/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "sawsbuck",
                "url": "https://pokeapi.co/api/v2/pokemon/586/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "bouffalant",
                "url": "https://pokeapi.co/api/v2/pokemon/626/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "rufflet",
                "url": "https://pokeapi.co/api/v2/pokemon/627/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "braviary",
                "url": "https://pokeapi.co/api/v2/pokemon/628/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "meloetta-aria",
                "url": "https://pokeapi.co/api/v2/pokemon/648/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "bunnelby",
                "url": "https://pokeapi.co/api/v2/pokemon/659/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "diggersby",
                "url": "https://pokeapi.co/api/v2/pokemon/660/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "fletchling",
                "url": "https://pokeapi.co/api/v2/pokemon/661/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "litleo",
                "url": "https://pokeapi.co/api/v2/pokemon/667/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "pyroar",
                "url": "https://pokeapi.co/api/v2/pokemon/668/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "furfrou",
                "url": "https://pokeapi.co/api/v2/pokemon/676/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "helioptile",
                "url": "https://pokeapi.co/api/v2/pokemon/694/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "heliolisk",
                "url": "https://pokeapi.co/api/v2/pokemon/695/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "pikipek",
                "url": "https://pokeapi.co/api/v2/pokemon/731/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "trumbeak",
                "url": "https://pokeapi.co/api/v2/pokemon/732/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "toucannon",
                "url": "https://pokeapi.co/api/v2/pokemon/733/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "yungoos",
                "url": "https://pokeapi.co/api/v2/pokemon/734/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "gumshoos",
                "url": "https://pokeapi.co/api/v2/pokemon/735/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "stufful",
                "url": "https://pokeapi.co/api/v2/pokemon/759/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "bewear",
                "url": "https://pokeapi.co/api/v2/pokemon/760/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "oranguru",
                "url": "https://pokeapi.co/api/v2/pokemon/765/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "type-null",
                "url": "https://pokeapi.co/api/v2/pokemon/772/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "silvally",
                "url": "https://pokeapi.co/api/v2/pokemon/773/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "komala",
                "url": "https://pokeapi.co/api/v2/pokemon/775/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "drampa",
                "url": "https://pokeapi.co/api/v2/pokemon/780/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "skwovet",
                "url": "https://pokeapi.co/api/v2/pokemon/819/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "greedent",
                "url": "https://pokeapi.co/api/v2/pokemon/820/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "wooloo",
                "url": "https://pokeapi.co/api/v2/pokemon/831/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "dubwool",
                "url": "https://pokeapi.co/api/v2/pokemon/832/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "obstagoon",
                "url": "https://pokeapi.co/api/v2/pokemon/862/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "indeedee-male",
                "url": "https://pokeapi.co/api/v2/pokemon/876/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "meloetta-pirouette",
                "url": "https://pokeapi.co/api/v2/pokemon/10018/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "kangaskhan-mega",
                "url": "https://pokeapi.co/api/v2/pokemon/10039/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "audino-mega",
                "url": "https://pokeapi.co/api/v2/pokemon/10069/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "pidgeot-mega",
                "url": "https://pokeapi.co/api/v2/pokemon/10073/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "lopunny-mega",
                "url": "https://pokeapi.co/api/v2/pokemon/10088/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "rattata-alola",
                "url": "https://pokeapi.co/api/v2/pokemon/10091/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "raticate-alola",
                "url": "https://pokeapi.co/api/v2/pokemon/10092/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "raticate-totem-alola",
                "url": "https://pokeapi.co/api/v2/pokemon/10093/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "gumshoos-totem",
                "url": "https://pokeapi.co/api/v2/pokemon/10121/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "zigzagoon-galar",
                "url": "https://pokeapi.co/api/v2/pokemon/10171/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "linoone-galar",
                "url": "https://pokeapi.co/api/v2/pokemon/10172/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "indeedee-female",
                "url": "https://pokeapi.co/api/v2/pokemon/10180/"
            },
            "slot": 2
        },
        {
            "pokemon": {
                "name": "meowth-gmax",
                "url": "https://pokeapi.co/api/v2/pokemon/10191/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "eevee-gmax",
                "url": "https://pokeapi.co/api/v2/pokemon/10196/"
            },
            "slot": 1
        },
        {
            "pokemon": {
                "name": "snorlax-gmax",
                "url": "https://pokeapi.co/api/v2/pokemon/10197/"
            },
            "slot": 1
        }
    ]
}
