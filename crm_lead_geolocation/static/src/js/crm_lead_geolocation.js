odoo.define('crm_lead_geolocation.CrmLeadGeolocation', ['owl', 'web.rpc'], function (require) {
    "use strict";

    // Import the necessary dependencies
    const { Component, mount } = require('owl');
    const { useState } = require('owl.hooks');
    const rpc = require('web.rpc');

    class GeolocationButton extends Component {
        constructor() {
            super(...arguments);
            this.state = useState({ latitude: null, longitude: null });
        }

        getGeolocation() {
            const self = this;
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (position) {
                    self.state.latitude = position.coords.latitude;
                    self.state.longitude = position.coords.longitude;
                    const recordId = self.props.recordId;
                    rpc.query({
                        model: 'crm.lead',
                        method: 'write',
                        args: [[recordId], { latitude: self.state.latitude, longitude: self.state.longitude }],
                    }).then(function () {
                        window.location.reload();
                    });
                });
            } else {
                alert("Geolocation is not supported by this browser.");
            }
        }
    }

    GeolocationButton.template = 'crm_lead_geolocation.GeolocationButton';

    // Mount the component after DOM is ready
    document.addEventListener('DOMContentLoaded', function () {
        const target = document.querySelector('.oe_button_get_geolocation');
        if (target) {
            mount(GeolocationButton, { props: { recordId: 1 }, target });
        }
    });

    return GeolocationButton;
});
