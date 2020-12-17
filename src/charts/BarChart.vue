<script>
import {HorizontalBar} from "vue-chartjs"

export default {
    extends: HorizontalBar,
    props:{
        labels:{
            type: Array
        },
        chartData:{
            type: Array
        },
        options:{
            type: Object
        }
    },
    data(){
        return{
        }
    },
    mounted(){
        this.renderChart({
            labels: this.labels,
            datasets: this.chartData
        }, this.options)
            
    }
}
</script>