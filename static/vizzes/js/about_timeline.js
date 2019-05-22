function showTime(){
    main = d3.select(".aboutsite")
    parseTime = d3.timeParse("%B %Y");
    formatTime = d3.timeFormat("%B '%y")

    d3.csv("https://gist.githubusercontent.com/Jasparr77/4f1f0fe8e08792dcf3cdf9ba089618b4/raw/50bd2793b4375ce689de86d9f6c57daf666cf2d6/aboutJasper.csv",function(data){

        data.forEach(function(d) {    
            d.start = parseTime(d.start)
            d.finish == "Today" ? d.finish = new Date() : d.finish = parseTime(d.finish)
        })

        console.log("data: ",data)

        vizSpace = main.append("svg")
        .style("height","450px")
        .style("width","800px")

        var y  = d3.scaleBand()
        .domain(['Skills','Focus','Work','Education'])
        .range([400,0])
        var yAxis = d3.axisLeft(y);
        
        var x = d3.scaleTime()
        .domain([new Date(2011, 8, 0, 0),new Date()])
        .range([0,720])
        var xAxis = d3.axisBottom(x);

        vizSpace.selectAll(".circle")
        .data(data).enter().append("circle")
            .attr("class",function(d){return d.type;})
            .attr("id",function(d){return d.name;})
            .attr("cy",function(d){return y(d.type);})
            .attr("cx",function(d){return x(d.start);})
            .attr("r",".5vw")
            .attr("transform","translate(80,50)")

        vizSpace.append("g")
        .attr("class","axis y")
        .attr("transform","translate(80,0)")
        .call(yAxis)

        vizSpace.append("g")
        .attr("class","axis x")
        .attr("transform","translate(80,400)")
        .call(xAxis)

    })
}
showTime()