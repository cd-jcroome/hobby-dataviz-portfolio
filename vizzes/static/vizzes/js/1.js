var margin = { top: 20, right: 20, bottom: 60, left: 50 };

var mainwidth = Math.max(document.documentElement.clientWidth, window.innerWidth || 0) - margin.left - margin.right,
	mainheight = (Math.max(document.documentElement.clientHeight, window.innerHeight || 0) - margin.top - margin.bottom)*.5;

var svg = d3.select(".mainviz").append("svg")
	.attr("width", mainwidth + margin.left + margin.right)
	.attr("height", mainheight + margin.top + margin.bottom);

var chartGroup = svg.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// d3.json("VizData").then(function (data) {
d3.csv("https://gist.githubusercontent.com/Jasparr77/eb2c35c5ba28e5480569cb87b1e5a3a9/raw/e4ad8475eb90688d5c04f65b26537b4b3aabd611/women_in_congress.csv").then(function (data){
	console.log(data)
	var y = d3.scaleLinear()
	.domain([0,d3.max(data,function(d){return d.women_total;})])
	.range([mainheight, 0]);

	var x = d3.scaleBand()
	.domain(data.map(function(d){ return d.years;}))
	.range([0, mainwidth])
	.paddingInner(.05)

	var yAxis = d3.axisLeft(y);

	var xAxis = d3.axisBottom(x).ticks(10)

	var line = d3.line()
	.x(function(d){ return x(d.years) ;})
	.y(function(d){ return y(d.women_total); })
	.curve(d3.curveNatural);

	var stack = d3.stack()
					.keys(["republican","democratic"])
					.order(d3.stackOrderNone)
					.offset(d3.stackOffsetNone);
	var datastack = stack(data);

	chartGroup.append("path")
		.attr("d",line(data))
		.attr("fill","none")
		.attr("class","totalCongress")  

	chartGroup.selectAll("circle.rep")
		.data(data)
		.enter().append("circle")
		.attr("class","rep")
		.attr("cx",function(d){return x(d.years);})
		.attr("cy",function(d){return y(d.republican);})
		.attr("r", (mainwidth/(208)))


	chartGroup.selectAll("circle.dem")
		.data(data)
		.enter().append("circle")
		.attr("class","dem")
		.attr("cx",function(d){return x(d.years);})
		.attr("cy",function(d){return y(d.democratic);})
		.attr("r", (mainwidth/(208)))

	chartGroup.append("g")
		.attr("class","axis y")
		.call(yAxis)

	chartGroup.append("g")
		.attr("class","axis x")
		.attr("transform","translate(0,"+mainheight+")")
		.call(xAxis)
		.selectAll("text")
		.attr("text-anchor","end")
		.attr("transform", "rotate(-90)")
});