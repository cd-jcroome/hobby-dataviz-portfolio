function showTime(){
    main = d3.select(".aboutsite")
    
    d3.csv("https://gist.githubusercontent.com/Jasparr77/4f1f0fe8e08792dcf3cdf9ba089618b4/raw/50bd2793b4375ce689de86d9f6c57daf666cf2d6/aboutJasper.csv",function(data){
        console.log("data: ",data)

        vizSpace = main.append("g")

        var y  = d3.scaleBand()
        .domain(data.map(function(d){return d.type}))
        .range([150,0])
        var yAxis = d3.axisLeft(y);

        var x = d3.scaleBand()
        .domain(data.map(function(d){return d.finish}))
        .range([0,400])
        var xAxis = d3.axisBottom(x);
        
        vizSpace.append("g")
        .attr("class","axis y")
        .call(yAxis)
        vizSpace.append("g")
        .attr("class","axis x")
        .call(xAxis)
    })
}
showTime()