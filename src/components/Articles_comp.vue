<template>
  <!-- eslint-disable max-len -->
  <div class='container'>
    <div class="row">
      <div class='col-sm-10'>
        <h1>Article</h1>
        <hr><br><br>
        <button type='button' class='btn btn-success btn-sm' v-b-modal.event-modal>Add Event</button>
        <br><br>
        <table class='table table-hover'>
          <thead>
            <tr>
              <th scope='col'>Name</th>
              <th scope='col'>Date</th>
              <th scope='col'>Lieu</th>
              <th scope='col'>Objet</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for='(event, index) in article' :key='index'>
              <td>{{ event.name }}</td>
              <td>{{ event.date }}</td>
              <td>{{ event.lieu }}</td>
              <td>{{ event.objet }}</td>
              <td>
                <div class='btn-group' role='group'>
                  <button type='button' class='btn btn-warning btn-sm'>Update</button>
                  <button type='button' class='btn btn-danger btn-sm'>Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addEventModal"
            id="event-modal"
            name="Add a new event"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addEventForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
         </b-form-group>
         <b-form-group id="form-date-group"
                       label="Date:"
                       label-for="form-date-input">
            <b-form-input id="form-date-input"
                          type="text"
                          v-model="addEventForm.date"
                          required
                          placeholder="Enter date">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-lieu-group"
                      label="Lieu:"
                      label-for="form-lieu-input">
            <b-form-input id="form-lieu-input"
                          type="text"
                          v-model="addEventForm.lieu"
                          required
                          placeholder="Enter lieu">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-objet-group"
                      label="Objet:"
                      label-for="form-objet-input">
            <b-form-input id="form-objet-input"
                          type="text"
                           v-model="addEventForm.objet"
                          required
                          placeholder="Enter objet">
            </b-form-input>
          </b-form-group>
          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Article1',
  data() {
    return {
      article: [],
      addEventForm: {
        name: '',
        date: '',
        lieu: '',
        objet: '',
      },
    };
  },
  methods: {
    getArticle() {
      const path = 'http://localhost:5000/article';
      axios
        .get(path)
        .then((res) => {
          this.article = res.data.article;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addEvent(payload) {
      const path = `http://localhost:5000/event/${payload.name}`;
      axios
        .post(path, payload)
        .then(() => {
          this.getArticle();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getArticle();
        });
    },
    initForm() {
      this.addEventForm.name = '';
      this.addEventForm.date = '';
      this.addEventForm.lieu = '';
      this.addEventForm.lieu = '';
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addEventModal.hide();
      const payload = {
        name: this.addEventForm.name,
        date: this.addEventForm.date,
        lieu: this.addEventForm.lieu,
        objet: this.addEventForm.objet,
      };
      this.addEvent(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.$refs.addEventModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getArticle();
  },
  console.log('test')
};
</script>