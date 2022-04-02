<script>
	import "./css/mapbox-gl.css";
	let webgl_canvas;

	export let width = "100%";
	export let height = "100%";
	let speak=true

	// import { default as mapboxgl } from "./mapbox-gl.js";
	import { default as AreaMap } from "./AreaMap.svelte";
	import mapboxgl, { Popup } from "mapbox-gl";
	import { onMount } from "svelte";

	import {
		mapsource,
		maplayer,
		mapfunctions,
	} from "./mapstore.js";


	console.log("mapboxgl", mapboxgl);

	

	async function init() {
		console.warn(webgl_canvas);



		// map setup and vars
		$mapsource = {
			area: {
				type: "vector",
				tiles: [
					`https://wolfiex.github.io/ONS_Maptiles/LSOA/{z}/{x}/{y}.pbf`,
				],
			}
		};

		$maplayer = [
			{
				id: "polygons",
				source: "area",
				"source-layer": 'processed_data',
				type: "fill",
				paint: {
					// "fill-color": "transparent",
					"fill-opacity": 0.7,
					"fill-outline-color": "steelblue",
				},
			},
		];


		if ('SpeechSynthesisUtterance' in window) {
			var msg = new SpeechSynthesisUtterance();
			console.error('speech tools enabled - "context menu". Use two finger click on mac trackpad to trigger');
		}


		$mapfunctions = [{event:'contextmenu',layer:'polygons',callback:(e)=>{
			if (speak){
			console.log(e.features[0].properties)
			var props = e.features[0].properties
			msg.text=props.name

			if (!window.speechSynthesis.speaking) {
				window.speechSynthesis.speak(msg);
			}
			
			}

		}

		}
		];

		


	} //endinit


	onMount(init);
</script>

<main>
	<div id="map">
		<AreaMap />
	</div>
</main>

<style>
	#map {
		width: 100%;
		height: auto;
		left: 0;
		margin: auto;
		position: absolute;
	}
	main {
		text-align: center;
		padding: 1em;
		margin: 0 auto;
	}

	
</style>
