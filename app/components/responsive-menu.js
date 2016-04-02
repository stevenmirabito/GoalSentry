import Ember from 'ember';

export default Ember.Component.extend({
    initializeMenu: function() {
        $('.right.menu.open').on("click", function (e) {
            e.preventDefault();
            $('.ui.vertical.menu').slideToggle();
        });

        $('.ui.dropdown').dropdown();
    }.on('didInsertElement')
});