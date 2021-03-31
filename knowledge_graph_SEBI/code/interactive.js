network.on("selectEdge", function (params) {
        if (params.edges.length === 1) {
            var edge = edges.get(params.edges[0]);
            window.open(edge.url, '_tab');
        }
    });
    
network.on("selectNode", function (params) {
        if (params.nodes.length === 1) {
            var node = nodes.get(params.nodes[0]);
            window.open(node.url, '_tab');
        }
    });
