<template>
    <Page class="page">
        <ActionBar title="Home" class="action-bar" />
        <ScrollView>
            <StackLayout>
                <Button text="Start Accelerometer" @tap="startAccelerometer"
                    :visibility="accelerometerValues.x ? 'collapsed' : 'visible'" />
                <StackLayout :visibility="accelerometerValues.x ? 'visible' : 'collapsed'">
                    <Label :text="'X: ' + accelerometerValues.x" />
                    <Label :text="'Y: ' + accelerometerValues.y" />
                    <Label :text="'Z: ' + accelerometerValues.z" />
                </StackLayout>
            
           <Button text="Stop Accelerometer" @tap="stopAccelerometer"
                    :visibility="accelerometerValues.x ? 'visible' : 'collapsed'" />
                    
        
                
             <GridLayout rows="*" height="1000px">
                <RadCartesianChart row="0">
                    <BarSeries v-tkCartesianSeries :items="categoricalSource"
                        categoryProperty="Name" valueProperty="Amount" />
                    <CategoricalAxis v-tkCartesianHorizontalAxis />
                    <LinearAxis v-tkCartesianVerticalAxis />
                </RadCartesianChart>
            </GridLayout>
            </StackLayout>

        </ScrollView>
    </Page>
</template>

<script>
import Vue from "nativescript-vue";
    import RadCartesianChart from "nativescript-ui-chart/vue";
    Vue.use(RadCartesianChart);
    const accelerometer = require("nativescript-accelerometer");
    let accelerometerListening = false;

    export default {
        methods: {
            startAccelerometer: function() {
                if (accelerometerListening) {
                    accelerometer.stopAccelerometerUpdates();
                }
                accelerometer.startAccelerometerUpdates(
                    data => {
                        accelerometerListening = true;
                        this.accelerometerValues = data;
                    }, {
                        sensorDelay: "ui"
                    }
                );
            },
            stopAccelerometer: function() {
                if (accelerometerListening) {
                    accelerometer.stopAccelerometerUpdates();
                    
                }
            },
            getX: function() {
                if (accelerometerListening) {
                    accelerometer.stopAccelerometerUpdates();
                    
                }
            }
        },

        data() {
            return {
                categoricalSource: [{
                        Name: "X-axis",
                        Amount: 2
                        //Amount: this.accelerometerValues.x
                       
                    },
                    {
                        Name: "Y-axis",
                        Amount: 2
                        //Amount: this.accelerometerValues.y
                    },
                    {
                        Name: "z-axis",
                        Amount: 2
                        //Amount: this.accelerometerValues.y
                    }
                   
                ],
                accelerometerValues: {
                    x: 0,
                    y: 0,
                    z: 0
                }
            };
        }
    };
</script>

<style scoped>
    .home-panel {
        vertical-align: center;
        font-size: 20;
        margin: 15;
    }

    .description-label {
        margin-bottom: 15;
    }
</style>