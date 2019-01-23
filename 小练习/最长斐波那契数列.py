# Author:ZJF
class Solution(object):
    def lenLongestFibSubseq(self, A):
        S = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):

                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0
print(Solution().lenLongestFibSubseq([3,9,14,22,23,32,37,52,54,59,60,67,68,69,71,74,76,77,82,84,85,96,97,99,100,101,113,118,138,140,145,152,157,161,167,170,176,178,204,219,222,246,254,258,271,274,275,280,356,360,364,398,407,411,441,447,451,452,560,582,583,653,656,712,726,727,916,942,947,1054,1060,1153,1174,1177,1178,1476,1524,1710,1713,1865,1901,1903,1904,2392,2466,2764,2773,3018,3075,3080,3082,3868,3990,4474,4486,4883,4976,4986,6260,6456,7238,7259,7901,8051,8068,10128,10446,11712,11745,12784,13027,13054,16388,16902,18950,19004,20685,21078,26516,27348,30662,30749,33469,34105,42904,44250,49612,49753,54154,55183,69420,71598,80274,80502,87623,89288,112324,115848,129886,130255,141777,144471,181744,187446,210160,210757,229400,233759,294068,303294,340046,341012,371177,378230,475812,490740,550206,551769,600577,611989,769880,794034,890252,892781,990219,1245692,1284774,1440458,1444550,1602208,1737563,1748182,2015572,2078808,2330710,2337331,2592427,3261264,3363582,3771168,3781881,4194635,5276836,5442390,5531581,6006413,6119212,6787062,8805972,9901093,10960359,10981697,11101020,11961598,12976360,14248362,14442420,14821434,15359202,15936648,16020305,19284185,21681839,22638357,23054334,24756215,24957247,25145810,25372355,25512030,25921398,27381620,27518473,28432766,28800930,29239260,30977016,31317897,32181690,32597170,33448471,34335563,35479655,35679653,36362380,40370235,41126782,42047464,44210863,45032676,45485453,45927401,46440611,47648021,48332713,51739879,53661087,54013763,55671099,59729554,61031400,61152946,62094075,63334100,63982252,64126215,67064863,68090430,68890150,69771650,70492097,73093292,73179931,73734016,73799297,76592074,78130473,78754798,80779631,82434243,83414845,85057940,85251139,88819311,89561647,90331595,92828269,93468391,94424903,95269536,96674583,99147115,99304223,100683780,101286921,102423259,106222561,107513954,110484789,112624349,113305153,113420780,114986792,115331335,116721365,116763864,119418978,120058202,123876716,124130078,124160561,124874359,125866935,127869582,128668997,130982132,131187052,131384155,132021146,134138723,135387833,137108804,140681630,141774984,142665527,144009028,146443879,149607927,150768349,151574645,155152577,155654187,157120970,160132832,160239672,160418454,160629526,162443201,162528946,162719409,163574244,165243500,166151622,167651444,167813760,167890012,169054168,170539766,170641609,170790480,171077223,171423306,173382749,173998398,179781823,179893993,180122344,182400879,183411374,183956080,184023701,186025822,186319462,186515028,187224835,189123445,191746044,192011848,192144662,192890972,193441337,193630982,194555696,194849625,197904750,198270074,198569232,199067326,199465362,205702616,205865378,206968102,207696508,208473827,208757599,211569286,211837048,212570096,213442202,214701108,216976425,217255176,217366958,217741564,218086772,218402158,220008410,223853002,224386961,225206489,226685222,228238345,228416869,230451582,231055196,231130722,231510218,234952848,235602988,235717603,238086790,238805521,239086781,243268500,245805104,247158300,249204106,259775936,259987335,260249539,260384651,260885593,262652406,265666827,265828471,267051983,268534122,269300646,269874004,270482169,271154775,273614210,275336225,276627875,277408629,277424909,278354125,280443227,282166665,283289408,287574811,288902764,289014555,289309389,290144124,290549876,290611941,291102434,292546319,292637906,293513631,294371513,294372456,295612903,298210528,298231632,298897287,299353983,300092115,300583166,301398973,301879226,303866189,305299176,305582067,307373674,307636141,310451055,311237942,312075188,312781745,313625496,314437215,315451863,317997185,318900555,323335434,324190312,324193002,324390157,327100855,327715138,329258352,329526730,331366326,332153447,334861288,334919104,336292270,338983665,339326621,340794440,343134217,344540424,345491570,345986797,346756539,347426753,347546502,348434394,349498903,349737700,350462422,350632994,352966259,352968622,354475635,354929134,355542822,358129016,368634316,369838051,370079072,373881839,373954283,375344485,376042404,376166339,377421127,378586103,381284493,381572471,381697337,382078685,383846673,384514494,385791639,385984975,386980639,388228381,388315594,389591731,389748396,391427423,392855032,393129880,393476156,393785983,394403010,397124802,397829750,397872372,398130330,398829626,400834600,401805213,402115549,403640403,403922823,404692701,405733259,406062999,407609872,411639501,412153217,413115262,413358795,413663015,415231706,415284345,416377968,416476929,419649117,420386675,421301058,422826407,423476028,423488105,423774920,424366277,424384242,424533280,428303226,428737660,429722455,430850087,431047948,431543995,434254977,437891125,444256040,445179701,445394151,446213524,446752005,446976526,447274635,447546836,448079510,449171431,450478112,453541063,454569482,456373151,456525339,458688929,459203799,459239886,460227301,460725799,462092719,462287754,462855242,466259040,467453533,471124586,471489242,471879750,472619678,473539760,474465284,475154773,477627399,478289343,481179241,481413353,481539702,484178863,486083981,486634675,488629431,491711700,492614022,493013046,495823042,497439685,497903345,501353684,502438951,503391447,503942300,505033754,505333139,506132576,507894840,508747923,509001679,509674032,510621750,511112199,511285772,515833466,516514806,517574195,518119196,519796017,521295921,521571537,524395807,525886399,528149235,529023126,529906344,530836243,531085418,533922222,534974451,535305241,535384563,535548874,535574596,539040129,542671046,546647847,547745392,548270336,548436248,548645879,548662022,550087614,557283503,558359552,559601039,561781533,564607942,565297595,566707449,566839708,569637045,571641073,571652665,571994891,572965547,573523994,579498811,580456390,581639381,582948099,584159197,584401490,584702789,584760550,586071668,587764056,588339315,589989660,590465192,590928739,593731029,595395274,595562376,595670800,596519380,600309560,601259745,603213139,603328730,606981637,607009433,608060863,609122190,616677864,617740113,617916927,619031974,619886375,620829667,620934603,621792998,623911099,624760661,626586872,627279143,628321548,630811914,633943674,636553833,636632055,638882815,640747313,640993950,644376879,644930626,646689712,649673488,650426322,651004783,651317354,652004353,653520887,658684970,659103743,660728885,661541578,661639585,663605197,664501184,665603955,667086941,667804041,668165106,669385393,669809644,670057129,672143142,673298706,673948111,674808417,675650974,676134763,676576872,678946752,681159669,682774760,684238880,685870135,690974789,692786917,695138203,696018334,696620553,696936056,697332689,697352393,699455242,699987754,704101924,708449168,708735620,710102900,713112993,714721675,715329058,716225241,717670686,721626624,722459082,724041483,724969219,726741093,727026507,727094693,728814527,730757329,730907708,731161428,732266782,732826958,733717130,736296761,736299693,736895365,736931921,739506069,744504260,746462832,746672738,749059556,749731819,750028939,750686307,750828744,753475548,754201596,755018294,756700967,757744441,759060552,759362853,760362696,761411808,762659358,765056061,765712275,767586006,767705753,769770100,769991745,770233582,776870049,777451070,777456024,778086260,778494988,779221108,779325867,780746435,782315675,783606009,784039066,784538268,785850603,789304147,790168521,790603227,792021838,792266532,793526745,793584461,794054179,795328015,800393689,804143278,805665592,809409635,811825394,811931490,815320990,817649382,818716102,823082360,823701604,826456896,826750366,828116759,828664001,828707090,829164135,832261636,832455610,835888967,835908269,836690684,837266363,837641293,838451281,839770827,840700413,842205827,842815791,844849706,846854520,848207519,849137841,849256184,850999212,851797196,852047422,852286866,852925801,852970204,853374990,853941941,855053502,856671585,856848452,856851714,857133817,857513419,857529764,859751212,863727103,864088001,864802579,865581180,869590528,870611028,873795712,874264022,879944610,883664714,885807712,889018012,890437972,890505222,891649570,891929768,893829620,893845899,894097188,894479562,894834620,896107400,896591606,896675526,898051334,898785698,898857049,899916301,901011198,904328179,904406351,904518674,904742091,905484932,906155231,906589224,908427712,909215205,911666265,912193648,915264085,917293384,918287028,919756036,924242630,925173009,925407377,926011655,926337494,927936720,928142475,929623066,930293302,930781786,931212840,931219192,932404877,934041585,937804436,938173245,939022548,939612015,941530685,941604005,943202966,943904045,944287568,944807066,948156608,949888275,950814572,951008692,952362711,952885221,952931935,952967767,954245205,956237342,956892501,957478826,958851125,959127049,960671631,961199142,961857541,962113078,965248622,966564339,970715056,973476038,973975773,977000076,978159310,980470939,980826297,981244308,982179297,984840092,984885883,987490164,988527907,989230340,989749199,989955771,990849052,990872873,992125893,992336688,992627088,993043544,995322102,996260709,998300525,999895841]))