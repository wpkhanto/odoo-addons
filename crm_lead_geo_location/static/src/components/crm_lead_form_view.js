/** @odoo-module */

import { registry } from "@web/core/registry"
import { formView } from "@web/views/form/form_view"
import { FormController } from "@web/views/form/form_controller"
import { useService } from "@web/core/utils/hooks";
const { onMounted } = owl

class CrmLeadFormController extends FormController {
    setup() {
        console.log("CRM Lead form inherited!")
        super.setup()
        // console.log(this.state);
        // console.log(Object.assign({}, this.model));
        // console.log(this.model.root.data.stage_id[1]);

        this.notification = useService("notification");

        onMounted(() => {
            this._registerEventListeners();
            this.disableFields();
        });

        // useEffect(() => {
        //     console.log(this)
        //     this.getLocation();
        // }, () => [])
    }

    _registerEventListeners() {
        const button = document.querySelector('button[name="get_geo_location"]');
        if (button) {
            button.addEventListener('click', this.getLocation.bind(this));
        }
    }

    getLocation() {
        if (navigator.geolocation) {
            const options = {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0,
            };

            const success = (pos) => {
                const crd = pos.coords;

                // console.log(`Latitude : ${crd.latitude}`);
                // console.log(`Longitude : ${crd.longitude}`);
                // console.log(`More or less ${crd.accuracy} meters.`);
                console.log(`lat, lng : ${crd.latitude}, ${crd.longitude}`);

                this._updateLeadLocation(crd.latitude, crd.longitude);
            }

            const error = (err) => {
                console.warn(`ERROR(${err.code}): ${err.message}`);
            }

            return navigator.geolocation.getCurrentPosition(success, error, options);
        }
        return;
    }

    async _updateLeadLocation(latitude, longitude) {


        // Get [id] from crm.lead
        const record = this.model.root.evalContext;
        const leadId = record.active_id;
        const payload = {
            lead_id: leadId,
            latitude: latitude,
            longitude: longitude,
        };
        // console.log('Payload being sent:', payload);

        try {
            const response = await fetch('/web/dataset/call_kw', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': odoo.csrf_token,
                },
                body: JSON.stringify({
                    jsonrpc: "2.0",
                    method: "call",
                    params: {
                        model: "crm.lead",
                        method: "write",
                        args: [
                            [leadId],
                            {
                                latitude: latitude,
                                longitude: longitude
                            }
                        ],
                        kwargs: {}
                    },
                    id: new Date().getTime()
                }),
            });

            const result = await response.json();
            if (result.result) {
                // Update the fields in the form.
                this.updateFields(latitude, longitude);

                this.notification.add("Lead location updated successfully", {
                    type: "success",
                });
            } else {
                this.notification.add("Failed to update lead location", {
                    type: "danger",
                });
                console.error("Failed to update lead location");
            }
        } catch (error) {
            this.notification.add("Error while updating lead location", {
                type: "danger",
            });
            console.error("Error while updating lead location", error);
        }
    }

    updateFields(latitude, longitude) {
        // Fack bind data this field.
        // Data on this field did not saved.
        const latField = document.querySelector('.latitude input');
        const lonField = document.querySelector('.longitude input');
        if (latField) { latField.value = latitude; latField.setAttribute("disabled", 1); }
        if (lonField) { lonField.value = longitude; lonField.setAttribute("disabled", 1); }
    }

    disableFields() {
        const latField = document.querySelector('.latitude input');
        const lonField = document.querySelector('.longitude input');
        if (latField) { latField.setAttribute("disabled", 1); }
        if (lonField) { lonField.setAttribute("disabled", 1); }
    }
}

const crmLeadFormView = {
    ...formView,
    Controller: CrmLeadFormController,
}

// Register the custom view for CRM Lead
registry.category("views").add("crm_lead_geo_location", crmLeadFormView)
