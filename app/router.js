import Ember from 'ember';
import config from 'goal-sentry/config/environment';

const Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('matches');
  this.route('rankings');
  this.route('live');
});

export default Router;
