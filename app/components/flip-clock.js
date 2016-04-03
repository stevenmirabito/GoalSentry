import Ember from 'ember';

export default Ember.Component.extend({
    clock: null,

    initialize: function() {
        this.clock = $('.flip-clock').FlipClock({
            autoStart: false,
            clockFace: 'Counter'
        });

        // Disable all links in the component
        $('.flip-clock a').bind("click.disable", function() { return false; });
    }.on('didInsertElement'),

    increment: function() {
        if (this.clock !== null) {
            this.clock.setTime(window.clock.getTime().time + 1);
        } else {
            console.log("[flip-clock] Can't increment a clock that has not been initialized.");
        }
    }
});