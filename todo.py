""" Basic todo list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/check', 'Check',
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    def GET(self):
        """ Show page """
        return "DriverInfo"

class Check:

    form = web.form.Form(
        web.form.Textbox('drvid', web.form.notnull, description="Driver ID:"),
        web.form.Button('Check'),
    )

    def GET(self):
        """ Show page """
        input_id = web.input(id='0')
        data_id = '0'
        data_input=web.data()
        if data_input:
            data_id=data_input.split("=")[1] 
        if data_id =='0' :
            data_id=input_id.id
        
        if data_id=='0':
            form = self.form()
            return render.index(form)
        else:
            output_driverinfo=model.get_driver(data_id)
            if output_driverinfo:
                return output_driverinfo
            else:
                return app.notfound() #404 not found
            

    def PUT(self):
        """ Show page """
        input_id = web.input(id='0')

        output_driverinfo=model.get_driver(input_id.id)
        if output_driverinfo:
            return output_driverinfo
        else:
            return app.notfound() #404 not found

    def POST(self):
        """ Show page """
        data = web.input()
        output_driverinfo=model.get_driver(data.drvid)
        if output_driverinfo:
            return output_driverinfo
        else:
            return app.notfound() #404 not found

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
