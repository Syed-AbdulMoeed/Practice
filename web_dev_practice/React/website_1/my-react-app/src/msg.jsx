
const Msg = function(props){

    return (
        <>
        {props.data.body && (
            <p>{props.data.body}</p>
        )}

        {props.data.display && (
            <ol>
                {props.data.display.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ol>
        )}
        </>
    )
}

export default Msg