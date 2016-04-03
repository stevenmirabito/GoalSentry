import Ember from 'ember';
import config from 'goal-sentry/config/environment';

export function siteConfig(params/*, hash*/) {
  if (config.APP.hasOwnProperty(params[0])) {
      return config.APP[params[0]];
  } else {
      console.log("[site-config] Unable to find site configuration property '" + params[0]+"'");
      return "";
  }
}

export default Ember.Helper.helper(siteConfig);
