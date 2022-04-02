import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';

import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"


function App() {
  const [description, setDescription] = useState("");
  const {register,handleSubmit,reset,formState:{errors}}=useForm()
  const [show,setShow]=useState(false)
  const [serverResponse,setServerResponse]=useState('')


  const userSubmit=(data)=>{


    console.log("data = ", data)

    const body = {
      description: data.description
  
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
        console.log(data)
        setServerResponse(data)
        setShow(true)
    })
    .catch(err => console.log(err))
    reset()
 }

  return (
    <Card>
        <Card.Body>
            <h2 className = "text-center mb-4 "> Login</h2>
            <Form>

                <Form.Group id = "description">
                    <Form.Label>Description</Form.Label>
                    <Form.Control 
                    type = "text" 
                    placeholder='description' 
                    {...register('description',{required:true})}
                    />
                </Form.Group>
                <br/>

                <br/>


                <Button onClick={handleSubmit(userSubmit)} className = "w-100" type  = "submit">Submit</Button>
            </Form>
        </Card.Body>
    </Card>

  );
}

export default App;
