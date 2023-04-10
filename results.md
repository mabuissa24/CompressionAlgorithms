# Results

## Compression Ratio

|Book|huff|digr256|digr512|digr1024|Z|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|booksconcatenated.txt|0.5604945840066509|0.5652089455437157|0.5749643832471912|0.6224565751926432|0.3885071904545888|
|COSC351Book9.txt|0.5534413092100621|0.5642071934146783|0.5736630084955068|0.6275231102943207|0.3986813402590071|
|COSC351Book8.txt|0.5551739521819589|0.5537669180673211|0.562174804849912|0.6107795180182202|0.40330666216134164|
|COSC351Book1.txt|0.5770561942145739|0.5818505709035975|0.5891774911980185|0.6299916141970555|0.3701997501373|
|COSC351Book3.txt|0.5595096140006154|0.5607416533624903|0.5693236724544786|0.6177350283448284|0.37171538702278284|
|COSC351Book2.txt|0.6133744026010536|0.5959994132961755|0.6015364306406072|0.6279992177282339|0.442221896275653|
|COSC351Book11.txt|0.5760216415537727|0.581714450142187|0.5877749377876378|0.6315784799401767|0.43638530633704625|
|COSC351Book6.txt|0.537780076089965|0.5502413227796584|0.5707676799439234|0.6261924882859777|0.32979374149392476|
|COSC351Book7.txt|0.585816124907985|0.5913031265739414|0.5928237960559452|0.633499283251327|0.4487791058076014|
|COSC351Book10.txt|0.5525951685226829|0.5618427076740773|0.5748724129108709|0.6279153144903923|0.3756025880990534|
|COSC351Book12.txt|0.5692011054265483|0.579192717818821|0.5809537812739138|0.6294816057423367|0.43683396212543985|
|COSC351Book5.txt|0.5677460500329163|0.5690558481457099|0.5726505924950626|0.6154542462146149|0.4293189049813474|
|COSC351Book4.txt|0.5532878152344943|0.5533734425395237|0.5613407292652873|0.6109690399600163|0.4018553190042212|
|Average (Excluding concatenated file)|0.5667502878|0.5702741137|0.5780882781|0.6240932455|0.403724497|

## Compression Time

|Book|huff|digr256|digr512|digr1024|Z|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|booksconcatenated.txt|2.159408808|11.26262093|59.72478008|37.67098594|3.572044849|
|COSC351Book9.txt|0.1017158031|0.3211882114|1.45907402|0.8535549641|0.1508581638|
|COSC351Book8.txt|0.0892791748|0.361191988|1.656507015|0.9981470108|0.1635417938|
|COSC351Book1.txt|0.5525140762|2.970592022|14.57458401|9.15734601|0.9044129848|
|COSC351Book3.txt|0.1514840126|0.7028410435|3.552900791|2.128179312|0.2639040947|
|COSC351Book2.txt|0.05754709244|0.1863749027|0.8117029667|0.5590910912|0.1038329601|
|COSC351Book11.txt|0.1214690208|0.5498542786|2.747832775|1.689286947|0.2168698311|
|COSC351Book6.txt|0.4193739891|2.123320103|10.63591099|7.275406837|0.653938055|
|COSC351Book7.txt|0.09631109238|0.416475296|2.091334105|1.326730013|0.176856041|
|COSC351Book10.txt|0.1244130135|0.552803278|2.534515142|1.460081816|0.2104401588|
|COSC351Book12.txt|0.07899808884|0.3000807762|1.44488883|0.9130706787|0.1443400383|
|COSC351Book5.txt|0.1532549858|0.7022500038|3.422050714|2.008060932|0.2624628544|
|COSC351Book4.txt|0.550812006|2.922684908|16.13083696|9.325818062|0.9523568153|
|TotalExcludingConcat|2.497172356|12.10965681|61.06213832|37.69477367|4.203813791|

## Decompression Time

|Book|huff|digr256|digr512|digr1024|Z|
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
|booksconcatenated.txt|4.492104769|40.2827642|36.16540527|35.38529897|853.2904389|
|COSC351Book9.txt|0.1453740597|1.03933692|0.9692730904|0.9434509277|39.50965977|
|COSC351Book8.txt|0.1570401192|1.175390959|1.075829029|1.064254284|41.00156522|
|COSC351Book1.txt|1.171580791|10.13840413|9.239419222|8.871388912|77.28481483|
|COSC351Book3.txt|0.2922222614|2.373552084|2.158349037|2.147273302|40.08681083|
|COSC351Book2.txt|0.09028697014|0.5668258667|0.5185940266|0.4941260815|14.97989607|
|COSC351Book11.txt|0.2272779942|1.828530073|1.635761976|1.570909739|263.5291841|
|COSC351Book6.txt|0.8699231148|7.251497984|6.670960903|6.692106962|42.85514379|
|COSC351Book7.txt|0.1803410053|1.389906883|1.214852095|1.197280884|47.77176285|
|COSC351Book10.txt|0.2319841385|1.839593172|1.693221807|1.679573059|69.21210599|
|COSC351Book12.txt|0.1336488724|0.9738161564|0.8849139214|0.851776123|38.09902906|
|COSC351Book5.txt|0.2950699329|2.319033861|2.07831192|2.002974987|85.80793405|
|COSC351Book4.txt|1.16962409|9.973543882|9.019545078|8.961452007|654.3306439|
|TotalExcludingConcat|4.96437335|40.86943197|37.15903211|36.47656727|1414.46855|