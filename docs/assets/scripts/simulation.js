function openPlay(evt, playName) {
  var i, tab_content, tab_links;

  tab_content = document.getElementsByClassName("tab-content");
  for (i = 0; i < tab_content.length; i++) {
    tab_content[i].style.display = "none";
  }
  tab_links = document.getElementsByClassName("tab-links");
  for (i = 0; i < tab_links.length; i++) {
    tab_links[i].className = tab_links[i].className.replace(" active", "");
  }

  document.getElementById(playName).style.display = "block";
  evt.currentTarget.className += " active";
}

// initialize global variables.
var edges;
var nodes;
var network;
var container;
var options, data;

let stageCounter = 1;

// This method is responsible for drawing the graph, returns the drawn network
function drawGraph(in_nodes, in_edges) {

  var container = document.getElementById('my-network');

  // parsing and collecting nodes and edges from the python
  nodes = new vis.DataSet(in_nodes);
  edges = new vis.DataSet(in_edges);

  // adding nodes and edges to the graph
  data = { nodes: nodes, edges: edges };

  var options = { "configure": { "enabled": false }, "nodes": { "font": { "size": 18 } }, "edges": { "arrows": { "to": { "enabled": true, "scaleFactor": 0.3 } }, "color": { "inherit": true }, "smooth": { "enabled": false, "type": "continuous" } }, "interaction": { "dragNodes": true, "hideEdgesOnDrag": false, "hideNodesOnDrag": false }, "physics": { "hierarchicalRepulsion": { "centralGravity": 0 }, "minVelocity": 0.75, "solver": "hierarchicalRepulsion" } };

  network = new vis.Network(container, data, options);

  return network;

}

function drawMain(){
  displayText('');
  drawGraph(main_nodes, main_edges);
  stageCounter = 1;
}

function displayText(playNum) {
  var i, div_class;

  div_class = document.getElementsByClassName("play");
  for (i = 0; i < div_class.length; i++) {
    div_class[i].style.display = "none";
  }

  if (playNum != '') {
    document.getElementById(playNum + "-turn-" + stageCounter).style.display = "block";
  }
}

function nextAction(playNum) {
  
  if (playNum == 'p1') {

    if (stageCounter > Object.keys(play1_nodes_dict).length){
      drawMain();
      return
    }
    
    displayText(playNum);
    nodes = play1_nodes_dict[stageCounter];
    edges = play1_edges_dict[stageCounter];
 
    drawGraph(nodes, edges);
    
    stageCounter += 1;
  }
  else if (playNum == 'p2') {
    if (stageCounter > Object.keys(play2_nodes_dict).length) {
      drawMain();
      return
    }

    displayText(playNum);
    nodes = play2_nodes_dict[stageCounter];
    edges = play2_edges_dict[stageCounter];

    drawGraph(nodes, edges);

    stageCounter += 1;
  }
}

function docReady(fn) {
  // see if DOM is already available
  if (document.readyState === "complete" || document.readyState === "interactive") {
    // call on next available tick
    setTimeout(fn, 1);
  } else {
    document.addEventListener("DOMContentLoaded", fn);
  }
}

// https://stackoverflow.com/questions/9899372/pure-javascript-equivalent-of-jquerys-ready-how-to-call-a-function-when-t
docReady(function () {
  // DOM is loaded and ready for manipulation here
  drawMain();
});


