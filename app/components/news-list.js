import Ember from 'ember';
import hbs from 'htmlbars-inline-precompile';
import connect from 'ember-redux/components/connect';

function stateToComputed(state) {
  return {
    news: state.news.all
  };
};

function dispatchToActions(dispatch) {
  return {
  };
};

var NewsListComponent = Ember.Component.extend({

});

export default connect(stateToComputed, dispatchToActions)(NewsListComponent);