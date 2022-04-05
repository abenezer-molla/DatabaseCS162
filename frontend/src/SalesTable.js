import React from 'react'
import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';
import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"

function SalesTable() {

    const [eventList, setEventList] = useState([]);
    const {reset}=useForm()
    const [show,setShow]=useState(false)
  
  
  
    useEffect(() => {
      //e.preventDefault();
      // GET request using fetch inside useEffect React hook
      fetch('/sales')
          .then(response => response.json())
          .then(data => {
            setEventList(data.event)
            console.log("LOOK HERE", data.event)
          }
  
          )   
  
  // empty dependency array means this effect will only run once (like componentDidMount in classes)
  }, []);
  return (
    <div className='stock-container'>
    
    <Card>

        <section>
            <h1> Sales Table</h1>

            {eventList.map(event => {
              return (
                <table>
                <tbody>
                <tr>
                        <th>Sales ID</th>
                        <th>Price in USD </th>
                        <th>Date Of Sale</th>
                        <th>created_at</th>
                    </tr>   
                  <tr key = {event.sales_id} >
                  <td>
                      <h5>{event.sales_id}</h5>
                    </td>

                    <td>
                      <h5>{event.price}</h5>
                    </td>
                    <td>
                      <h5>{event.date_of_sale}</h5>
                    </td>
                    <td>
                      <h5>{event.created_at}</h5>
                    </td>
                
                  </tr>
                </tbody>
              </table>
               
         

              )
            })}

      
        </section>

    </Card>

    </div>
  )
}

export default SalesTable