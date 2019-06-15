const india = new google.maps.LatLng(20.5937, 78.9629);
const initMap = () => {
    const map = new google.maps.Map(document.getElementById('map'), {
        center: india,
        zoom: 4.5
    });
    return map
}

const plotHeatMap = (map, data, color) => {
    heatmap = new google.maps.visualization.HeatmapLayer({
        data,
        map
    });
    heatmap.set('gradient', [color])
    heatmap.set('opacity', 0.2)
    return heatmap;
}

console.log("hello")