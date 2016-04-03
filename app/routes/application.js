import Ember from 'ember';
import config from 'goal-sentry/config/environment';

export default Ember.Route.extend({
    title: function(tokens) {
        return tokens.join(' - ') + ' - ' + config.APP.name;
    }
});
