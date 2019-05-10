function resize() {
    const height = (window.innerHeight*.95)
    const width = (window.innerWidth*.95)

    headerHeight = Number(d3.select(".header").style('height').slice(0,-2));
    footerHeight = +Number(d3.select(".footer").style('height').slice(0,-2)) +Number(d3.select(".footerContactBar").style('height').slice(0,-2));
    vizDescHeight = Number(d3.select(".vizDesc").style('height').slice(0,-2));
    console.log("header: ",headerHeight,"footer: ",footerHeight,"desc: ",vizDescHeight)
    console.log(headerHeight+footerHeight+vizDescHeight)
    // About resize
    aboutSite = d3.select(".aboutsite")
        
    aboutSite.style("height",(height-(footerHeight+headerHeight))+"px")

    // Tableau resize
    tableauPlaceHolder = d3.select(".tableauPlaceholder")
    tableauViz = d3.select(".tableauViz")

    tableauPlaceHolder
        .style("height",((height)-(headerHeight+vizDescHeight+footerHeight))+"px")
        .style("top",(headerHeight+vizDescHeight)+"px")
        .style("width",width+"px")

    tableauViz
        .style("height",(height-(headerHeight+vizDescHeight+footerHeight))+"px")
        .style("width",width+"px")


    // Static D3 resize
    body = d3.select("#staticBody")

    body
        .style("top",(vizDescHeight+headerHeight)+"px")
        .style("width",(width)+"px")
};

resize()