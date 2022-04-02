import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';

import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"


function App() {
  const [description, setDescription] = useState("")
  const [eventList, setEventList] = useState([]);
  const {reset}=useForm()
  const [show,setShow]=useState(false)
  const [serverResponse,setServerResponse]=useState('')




  const handleChange = (e) =>{
    e.preventDefault();
    setDescription(e.target.value);

  }

  const handleSubmit = (e) =>{
    
    e.preventDefault();

    console.log(description)
  

  const body = {
    description: description
  }

const requestOptions = {
    method: "POST",
    headers: {
        'content-type': 'application/json'
    },
    body: JSON.stringify(body)

}



fetch('/event', requestOptions)
    .then(res => res.json())
    .then(data =>{
        const {events} = data
        setEventList(events)
        console.log("THIS IS THE PRINT", eventList)
        setShow(true)
    })

  

  }

  useEffect(() => {
    //e.preventDefault();
    // GET request using fetch inside useEffect React hook
    fetch('/event')
        .then(response => response.json())
        .then(data => {
          setEventList(data.event)
          console.log("LOOK HERE", data.event)
        }

        )
    

// empty dependency array means this effect will only run once (like componentDidMount in classes)
}, []);

  return (
    
    <Card>
        <section> 
        <Card.Body>
            <h2 className = "text-center mb-4 "> Login</h2>
            <Form onSubmit = {handleSubmit} >

                <Form.Group id = "description">
                    <Form.Label>Description</Form.Label>
                    <Form.Control 
                    type = "text" 
                    name = "description"
                    placeholder='description' 
                    onChange = {handleChange}
                    />
                </Form.Group>
                <br/>

                <br/>


                <Button type = "submit" className = "w-100">Submit</Button>
                
            </Form>
        </Card.Body>
        </section>

        <section>
          <ul>
          {eventList.map(event => {
              return (
                <li key = {event.id}>
                    {event.description}
                </li>

              )
            })}

          </ul>

        </section>

    </Card>
    





  );
}

export default App;
