import Ember from 'ember';
import config from 'goal-sentry/config/environment';

export default Ember.Route.extend({
    title: config.APP.name,
    beforeModel: function() {
        this.transitionTo('matches');
    }
});
