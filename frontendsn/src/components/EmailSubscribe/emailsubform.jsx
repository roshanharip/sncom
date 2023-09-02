
import axios from 'axios';
import { API_URL } from '../../constants/ApiUrl';
import React, {  useState } from 'react';
import { Form, FormGroup, Label, Input, Button } from 'reactstrap';
const EmailSubForm  = () => {
    const [subscriber, setSubscriber] = useState({
        name : '',
        email: '',
        phone: '',
        })

    const onHandleData = (evt) => {
        const {target} = evt;
        const {name, email, phone} = target;
        setSubscriber({name : name.value, email : email.value, phone : phone.value});
        axios.post(API_URL, subscriber)
        evt.preventDefault();
        Handle();
    };
    const Handle = () => {
        console.log(subscriber);
    }
    const onChangeHandle = (evt) => {
        setSubscriber({[evt.target.name] : evt.target.value});
    }
    return (
        <Form onSubmit={onHandleData}>
          <FormGroup>
            <Label for="name">Name:</Label>
            <Input
              type="text"
              name="name"
              onChange={onChangeHandle}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label for="email">Email:</Label>
            <Input
              type="email"
              name="email"
              onChange={onChangeHandle}
              required
            />
          </FormGroup>
          <FormGroup>
            <Label for="phone">Phone:</Label>
            <Input
              type="text"
              name="phone"
              onChange={onChangeHandle}
              required
            />
          </FormGroup>
          <Button >Send</Button>
        </Form>
      );
}
export default EmailSubForm;