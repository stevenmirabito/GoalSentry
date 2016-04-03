import Ember from 'ember';
import config from 'goal-sentry/config/environment';

const Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('scoreboard');
  this.route('matches');
  this.route('rankings');
});

export default Router;
